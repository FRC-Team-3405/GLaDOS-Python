from commands2 import Command
from components.drive.config import Swerve_constants
from wpimath.geometry import Translation2d

class TeleopSwerve(Command):
    def __init__(self,swerve:object,translationSup:float,strafeSup:float, rotationSup:float, robotCentricSup:bool):
        self.swerve = swerve
        self.addRequirements(self.swerve)
        self.translationSup = translationSup
        self.strafeSup = strafeSup
        self.rotationSup = rotationSup
        self.robotCentricSup = robotCentricSup
    
    def execute(self):
        # Get Values, Deadband
        if abs(self.translationSup) > Swerve_constants.stickDeadband:
            translationVal = self.translationSup
        else:
            translationVal = self.translationSup

        if abs(self.rotationSup) > Swerve_constants.stickDeadband:
            rotationVal = self.translationSup
        else:
            rotationVal = self.translationSup

        if abs(self.strafeSup) > Swerve_constants.stickDeadband:
            strafeVal = self.translationSup
        else:
            strafeVal = self.translationSup

        # Drive
        self.swerve.drive(
            Translation2d(translationVal * Swerve_constants.maxSpeed, strafeVal * Swerve_constants.maxSpeed), 
            rotationVal * Swerve_constants.maxAngularVelocity, 
            self.robotCentricSup,
            True
        )