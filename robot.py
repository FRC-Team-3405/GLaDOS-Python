import wpilib._wpilib as cool
from wpilib import PowerDistribution, TimedRobot, SendableChooser, Timer, run, DriverStation
from ntcore._ntcore import NetworkTableInstance
from robotcontainer import RobotContainer
from commands2 import *

class Robot(TimedRobot):
    def robotInit(self):
    
        self.team = DriverStation.getAlliance()
        self.pdp = PowerDistribution()
        self.m_robotContainer = RobotContainer()
        
        self.smartdashboard = cool.SmartDashboard
        self.networktable_inst = NetworkTableInstance.getDefault()
        self.networktable_inst.setServer("Rio")
        self.datatable = self.networktable_inst.getTable("data")
        self.limelight = self.networktable_inst.getTable("limelight")
        self.almost_there = self.datatable.getStringTopic("greeting").publish()

        self.controller1_choice = SendableChooser()
        self.controller1_choice.setDefaultOption("Xbox controller","Xbox")
        self.controller1_choice.addOption("Ps4 controller","PS4")
        self.controller1_choice.addOption("Joystick","Joystick")

        self.autonomous_chooser = SendableChooser()
        self.autonomous_chooser.setDefaultOption("Drive_forward","Drive_forward")
        self.autonomous_chooser.addOption("SPIN!!!","SPIN")

        self.smartdashboard.putData("Autonomous", self.autonomous_chooser)
        self.smartdashboard.putData("Controller1", self.controller1_choice)
        


    def disabledInit(self):
        pass

    def autonomousInit(self):
        self.timer = Timer()
        self.timer.start()

    def teleopInit(self):
        self.almost_there.set("Hello") # Puts data into the network tables

    def testInit(self):
        pass

    def robotPeriodic(self):
        CommandScheduler.getInstance().run()

    def disabledPeriodic(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopPeriodic(self):

        self.smartdashboard.putNumber("Total Power Usage",self.pdp.getTotalPower())
        self.almost_there.set("Hello") # Puts data into the network tables
        
    def testPeriodic(self):
        pass


if __name__ == "__main__":
    run(Robot)
