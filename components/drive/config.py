from wpimath.geometry import Transform2d,Rotation2d,Translation2d
from wpimath.trajectory import TrapezoidProfile
from wpimath.kinematics import SwerveDrive2Kinematics,SwerveDrive3Kinematics,SwerveDrive4Kinematics,SwerveDrive6Kinematics
from frc.util.COTSTalonFXSwerveConstants import *
from phoenix6.signals import NeutralModeValue
from wpimath import units
import math

class SwerveModuleConstants:
    def __init__(self, module_num, driveMotorID, angleMotorID, canCoderID, angleOffset):
        self.module_num = module_num
        self.driveMotorID = driveMotorID
        self.angleMotorID = angleMotorID
        self.canCoderID = canCoderID
        self.angleOffset = angleOffset

class Swerve_constants():
    def __init__(self):
        pass
    pigeonID = 20
    invertGyro = False

    #TODOx: This must be tuned to specific robot
    chosenModule = SDS.MK4i.Falcon500(SDS.MK4i.driveRatios.L2)

    # Drivetrain Constants
    trackWidth = units.inchesToMeters(24.5)
    wheelBase = units.inchesToMeters(24.5)
    wheelDiameter = units.inchesToMeters(4.0)
    wheelCircumference = chosenModule.wheelCircumference

    openLoopRamp = 0.25
    closedLoopRamp = 0.0

    driveGearRatio = chosenModule.driveGearRatio
    angleGearRatio = chosenModule.angleGearRatio

    swerveKinematics = SwerveDrive4Kinematics(
        Translation2d(wheelBase / 2.0, trackWidth / 2.0),
        Translation2d(wheelBase / 2.0, -trackWidth / 2.0),
        Translation2d(-wheelBase / 2.0, trackWidth / 2.0),
        Translation2d(-wheelBase / 2.0, -trackWidth / 2.0)
        )
    
    # Swerve Voltage Compensation
    voltageComp = 12.0

    # Swerve Angle Current Limiting
    angleCurrentLimit = 15
    angleCurrentThreshold = 30
    angleCurrentThresholdTime = 0.1
    angleEnableCurrentLimit = True

    # Swerve Drive Current Limiting
    driveCurrentLimit = 20
    driveCurrentThreshold = 40
    driveCurrentThresholdTime = 0.1
    driveEnableCurrentLimit = True

    angleMotorInvert = chosenModule.angleMotorInvert
    driveMotorInvert = chosenModule.driveMotorInvert

    #Angle Motor PID Values
    angleKP = chosenModule.angleKP
    angleKI = chosenModule.angleKI
    angleKD = chosenModule.angleKD

    # Drive Motor PID Values
    driveKP = 0.1
    driveKI = 0.0
    driveKD = 0.0
    driveKFF = 0.0

    # Drive Motor Characterization Values
    driveKS = 0.32
    driveKV = 1.51
    driveKA = 0.27

    # Drive Motor Conversion Factors
    driveConversionPositionFactor = (wheelDiameter * math.pi) / driveGearRatio
    driveConversionVelocityFactor = driveConversionPositionFactor / 60.0
    angleConversionFactor = 360.0 / angleGearRatio

    # Swerve Profiling Values
    maxSpeed = 4.5
    maxAngularVelocity = 11.5

    # Neutral Modes 
    angleNeutralMode = NeutralModeValue.COAST
    driveNeutralMode = NeutralModeValue.BRAKE

    driveInvert = chosenModule.driveMotorInvert
    angleInvert = chosenModule.angleMotorInvert

    canCoderInvert = chosenModule.cancoderInvert

    stickDeadband = 0.1

    def MOD0():
        driveMotorID = 1
        angleMotorID = 2
        canCoderID = 17
        angleOffset = Rotation2d.fromDegrees(11.25)
        return SwerveModuleConstants(0,driveMotorID, angleMotorID, canCoderID, angleOffset)
    
    def MOD1():
        driveMotorID = 3
        angleMotorID = 4
        canCoderID = 18
        angleOffset = Rotation2d.fromDegrees(-93.25)
        return SwerveModuleConstants(1,driveMotorID, angleMotorID, canCoderID, angleOffset)
    
    def MOD2():
        driveMotorID = 5
        angleMotorID = 6
        canCoderID = 16
        angleOffset = Rotation2d.fromDegrees(-42.45)
        return SwerveModuleConstants(2,driveMotorID, angleMotorID, canCoderID, angleOffset)
    
    def MOD3():
        driveMotorID = 7
        angleMotorID = 8
        canCoderID = 19
        angleOffset = Rotation2d.fromDegrees(55.89)
        return SwerveModuleConstants(3,driveMotorID, angleMotorID, canCoderID, angleOffset)
    
class AutonomousConstants:
    kMaxSpeedMetersPerSecond = 3
    kMaxAccelerationMetersPerSecondSquared = 3
    kMaxAngularSpeedRadiansPerSecond = math.pi
    kMaxAngularSpeedRadiansPerSecondSquared = math.pi

    kPXController = 1
    kPYController = 1
    kPThetaController = 1

    kThetaControllerConstraints = TrapezoidProfile.Constraints(kMaxAngularSpeedRadiansPerSecond,kMaxAngularSpeedRadiansPerSecondSquared)