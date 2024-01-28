from wpimath.kinematics import SwerveDrive2Odometry,ChassisSpeeds,SwerveDrive4Kinematics,SwerveModuleState
from wpimath.geometry import Pose2d
from wpilib import SmartDashboard,Field2d,DriverStation
from components.drive.controllers import *
from components.drive.config import *
from components.drive.motors import *
from components.drive.MiscCAN import *
from components.drive.driveMotorGroup import *
from pathplannerlib.auto import AutoBuilder, HolonomicPathFollowerConfig, ReplanningConfig
from pathplannerlib.controller import PIDConstants
from commands2 import Subsystem

SwerveModuleState.speed_fps
class Swerve(Subsystem):
    def __init__(self):
        self.gyros = Pigeon2(Swerve_constants.pigeonID)
        self.center_gyros()
        self.swerve_modules = [
            Swerve_module(Swerve_constants.MOD0()),
            Swerve_module(Swerve_constants.MOD1()),
            Swerve_module(Swerve_constants.MOD2()),
            Swerve_module(Swerve_constants.MOD3()),
        ]
        self.swerveOdometry = SwerveDrive4Odometry(Swerve_constants.swerveKinematics,self.getGyroYaw(),self.getModulePositions(),Pose2d())
        self.field = Field2d()
        SmartDashboard.putData("Field", self.field)

        self.autobuilder = AutoBuilder.configureHolonomic(
            self.getPose, # Robot pose supplier
            self.setPose, # Method to reset odometry (will be called if your auto has a starting pose)
            self.getChasisHeading, # ChassisSpeeds supplier. MUST BE ROBOT RELATIVE
            self.driveRobotRelative,
            config=HolonomicPathFollowerConfig(
                PIDConstants(5.0, 0.0, 0.0), # Translation PID constants
                PIDConstants(5.0, 0.0, 0.0),
                3.5, # Max module speed, in m/s
                0.4, # Drive base radius in meters. Distance from robot center to furthest module.
                ReplanningConfig()
            ),
            should_flip_path = self.get_alliance(),
            drive_subsystem=self
        )

    def driveRobotRelative(self, stuff):
        # Calculates the neccicary speeds and angles to set the motors too, uses WPILIB's swerveKinematics code, Robot Relative
        swerveModuleStates = Swerve_constants.swerveKinematics.toSwerveModuleStates(stuff)
        # Enforce the max speed of the robot
        SwerveDrive2Kinematics.desaturateWheelSpeeds(swerveModuleStates, Swerve_constants.maxSpeed)
        # for each module, set the desired state to what the swerveKinematics code dictates
        for SwerveModule in self.swerve_modules:
            SwerveModule.setDesiredState(swerveModuleStates[SwerveModule.moduleNumber].speed_fps * 0.3048, False)

    def get_alliance(self):
        return DriverStation.getAlliance() == DriverStation.Alliance.kRed
    
    def getGyroYaw(self):
        if Swerve_constants.invertGyro == True:
            return Rotation2d.fromDegrees(360 - self.gyros.get_yaw())
        else:
            return Rotation2d.fromDegrees(self.gyros.get_yaw())
            
    
    def zeroHeading(self):
        self.swerveOdometry.resetPosition(self.getGyroYaw(), self.getModulePositions(), Pose2d(self.getPose().X(),self.getPose().Y(), Rotation2d()));
    

    def drive(self,translation, rotation, fieldRelative, isOpenLoop):
        """ Calculates the neccicary speeds and angles to set the motors too, uses WPILIB's swerveKinematics code"""
        if fieldRelative:
            chassis_speeds = ChassisSpeeds.fromFieldRelativeSpeeds(
                                    translation.X(),
                                    translation.Y(),
                                    rotation,
                                    self.getHeading()
                                )
        else:
            chassis_speeds = ChassisSpeeds(
                        translation.X(),
                        translation.Y(),
                        rotation
                        )

        swerveModuleStates = Swerve_constants.swerveKinematics.toSwerveModuleStates(chassis_speeds)
        # Enforce the max speed of the robot
        SwerveDrive4Kinematics.desaturateWheelSpeeds(swerveModuleStates, Swerve_constants.maxSpeed)
        # For each module, set the desired state to what the swerveKinematics code dictates
        for SwerveModule in self.swerve_modules:
            SwerveModule.setDesiredState(swerveModuleStates[SwerveModule.moduleNumber], isOpenLoop)

    def setPose(self,pose):
        self.swerveOdometry.resetPosition(self.getGyroYaw(), self.getModulePositions(), pose)

    def getHeading(self):
        return self.getPose()

    def getModulePositions(self):
        positions = []
        for SwerveModule in self.swerve_modules:
            positions.append(SwerveModule.getPosition())
        positions = tuple(positions)
        return positions
        
    def setModuleStates(self,desiredStates):
        SwerveDrive2Kinematics.desaturateWheelSpeeds(desiredStates, Swerve_constants.maxSpeed)
        for SwerveModule in self.swerve_modules:
            SwerveModule.setDesiredState(self.swerveModuleStates[SwerveModule.moduleNumber], False)
    
    def center_gyros(self):
        self.gyros.reset()

    def setHeading(self,heading):
        self.swerveOdometry.resetPosition(self.getGyroYaw(), self.getModulePositions(), Pose2d(self.getPose().X(),self.getPose().Y(), heading))

    def update(self,fieldRelative,translation,rotation,isOpenLoop):
        if fieldRelative == True:
            chassis_speed = ChassisSpeeds.fromFieldRelativeSpeeds(translation.X(), translation.Y(), rotation, self.getGyroYaw())
        else:
            chassis_speed = ChassisSpeeds(translation.X(), translation.Y(), rotation)
        self.swerveModuleStates = Swerve_constants.swerveKinematics.toSwerveModuleStates(chassis_speed)
        SwerveDrive2Kinematics.desaturateWheelSpeeds(self.swerveModuleStates, Swerve_constants.maxSpeed)

        for SwerveModule in self.swerve_modules:
            SwerveModule.setDesiredState(self.swerveModuleStates[SwerveModule.moduleNumber], isOpenLoop)

    def getPose(self):
        return self.swerveOdometry.getPose()
    
    def getModuleStates(self): 
        states = []
        for module in self.swerve_modules:
            states.append(Swerve_constants.swerveKinematics.toSwerveModuleStates(module.getState()))
        return states
    
    def getChasisHeading(self):
        now = self.getPose()
        return ChassisSpeeds.fromFieldRelativeSpeeds(
                                    now.X(), 
                                    now.Y(), 
                                    now.rotation().radians(), 
                                    self.getHeading()
                                )
    
    def resetModulesToAbsolute(self):
        for module in self.swerve_modules:
            module.resetToAbsolute()

    def periodic(self):
        self.swerveOdometry.update(self.getGyroYaw(), self.getModulePositions())
        self.field.setRobotPose(self.getPose())
        for module in self.swerve_modules:
            
            SmartDashboard.putNumber(f"Mod {module.moduleNumber} Cancoder", module.getCANcoder().degrees().real)
            SmartDashboard.putNumber(f"Mod {module.moduleNumber} Integrated", module.getState().angle.degrees().real)
            SmartDashboard.putNumber(f"Mod {module.moduleNumber} Velocity", module.getState().angle.degrees().real)