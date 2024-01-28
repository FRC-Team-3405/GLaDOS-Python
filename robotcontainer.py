from components.drive.driveBase import Swerve
from components.drive.controllers import *
from TeleopSwerve import TeleopSwerve
from commands2 import instantcommand,command
from wpilib import SmartDashboard
from wpilib.interfaces import GenericHID

class RobotContainer():
    def __init__(self) -> None:
        self.drive_usb = GenericHID(0)
        self.driver_controller = Xbox_controller()
        self.swerve = Swerve()
        self.swerve.setDefaultCommand(
            TeleopSwerve(
                self.swerve,
                self.drive_usb.getRawAxis(self.driver_controller.AxisMap["LeftY"]),
                self.drive_usb.getRawAxis(self.driver_controller.AxisMap["LeftX"]),
                self.drive_usb.getRawAxis(self.driver_controller.AxisMap["RightX"]),
                self.drive_usb.getRawButtonPressed(self.driver_controller.ButtonMap["Centric"])
            )
        )
        if self.drive_usb.getRawButtonPressed(self.driver_controller.ButtonMap["Center"]):
            instantcommand(self.swerve.zeroHeading())