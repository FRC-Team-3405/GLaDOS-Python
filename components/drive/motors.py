import wpilib
from wpimath.controller import *
from phoenix6 import controls, configs, hardware, signals

class CANMotor:
    def __init__(self,_id) -> None:
        self.talonfx = hardware.TalonFX(_id)
        self.talonfx_configurator = self.talonfx.configurator

    def set(self,set_value):
        self.talonfx.set_control(controls.DutyCycleOut(set_value).output)

    def getVelocity(self) -> float:
        return self.talonfx.get_velocity().value
    
    def getPosition(self):
        return self.talonfx.get_position().value
        
    def get_pid(self):
        return PIDController
    
    def setPosition(self,set_value):
        self.talonfx_configurator.set_position(set_value)

class PWMSpark:
    def __init__(self, _id: int, _invert: bool):
        self.motor = wpilib.Spark(_id)
        self.motor.setInverted(_invert)

    def set(self,value: float):
        self.motor.set(value)

    def getVelocity(self) -> float:
        pass