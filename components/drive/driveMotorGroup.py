from components.drive.motors import *
from components.drive.MiscCAN import *
from components.drive.driveMotorGroup import *
from components.drive.CTREconfigs import *
from frc.math.Conversions import Conversions
from wpimath.controller import SimpleMotorFeedforwardMeters
from wpimath.kinematics import SwerveModuleState
from wpimath.kinematics import *
from phoenix6 import controls

class Swerve_module():
    def __init__(self,swerve_constants) -> None:
        self.driveFeedForward = SimpleMotorFeedforwardMeters(Swerve_constants.driveKS,Swerve_constants.driveKV,Swerve_constants.driveKA)

        # Drive motor control requests
        self.driveDutyCycle = controls.DutyCycleOut(0)
        self.driveVelocity = controls.VelocityVoltage(0)

        # Angle motor control requests
        self.anglePosition = controls.PositionVoltage(0)

        # Swerve module config
        self.angleOffset = swerve_constants.angleOffset
        self.moduleNumber = swerve_constants.module_num

        # Angle encoder
        self.angleEncoder = CANcoder(swerve_constants.canCoderID)
        self.angleEncoder.configurator.apply(CTREConfigs.swerveCANcoderConfig) 

        # Angle motor
        self.angleMotor = CANMotor(swerve_constants.angleMotorID)
        self.angleMotor.talonfx_configurator.apply(CTREConfigs.swerveAngleFXConfig)

        # Drive motor
        self.driveMotor = CANMotor(swerve_constants.driveMotorID)
        self.driveMotor.talonfx_configurator.apply(CTREConfigs.swerveDriveFXConfig)
        self.driveMotor.talonfx_configurator.set_position(0.0)

        self.feedforward = SimpleMotorFeedforwardMeters(Swerve_constants.driveKS,Swerve_constants.driveKV,Swerve_constants.driveKA)

        self.lastAngle = self.getState().angle

    def setDesiredState(self,desiredState,isOpenLoop):
        #Optomises the desired state, so that the wheel doenst have to turn more than 90 degrees
        desiredState = SwerveModuleState.optimize(desiredState, self.getState().angle)
        # snap the angle motor to the desired angle
        self.angleMotor.setPosition(self.anglePosition.with_position(desiredState.angle.degrees()).position)
        # set the speed of the drive motor
        self.setSpeed(desiredState.speed_fps * 0.3048, isOpenLoop)

    def setSpeed(self,desiredState,isOpenLoop):
        if isOpenLoop:
            self.driveDutyCycle.output = desiredState / Swerve_constants.maxSpeed
            self.driveMotor.set(self.driveDutyCycle)
        else:
            self.driveVelocity.velocity = Conversions.MPSToRPS(desiredState, Swerve_constants.wheelCircumference)
            self.driveVelocity.feed_forward = self.driveFeedForward.calculate(desiredState)
            self.driveMotor.set(self.driveVelocity)

    def getCANcoder(self): 
        return Rotation2d.fromDegrees(self.angleEncoder.getAbsolutePosition()  * 360)
    
    def resetToAbsolute(self):
        absolutePosition = self.getCANcoder() - self.angleOffset
        self.angleMotor.setPosition(absolutePosition)

    def getState(self): 
        return SwerveModuleState(
            Conversions.RPSToMPS(self,self.driveMotor.getVelocity(), Swerve_constants.wheelCircumference), 
            Rotation2d.fromDegrees(self.angleMotor.getPosition() * 360)
            )
    
    def getPosition(self):
        return SwerveModulePosition(
            Conversions.rotationsToMeters(self.driveMotor.getPosition(), Swerve_constants.wheelCircumference), 
            Rotation2d.fromDegrees(self.angleMotor.getPosition() * 360)
            )