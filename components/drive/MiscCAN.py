from phoenix6 import signals, hardware, controls, configs
from components.drive.config import *

class Pigeon2:
    def __init__(self,_id) -> None:
        self.gyros = hardware.pigeon2.Pigeon2(_id)

    def reset(self):
        self.gyros.set_yaw(0)

    def get_yaw(self):
        return self.gyros.get_yaw().value

class CANcoder:
    def __init__(self,_id) -> None:
        self.encoder = hardware.CANcoder(_id)
        self.configurator = self.encoder.configurator

    def getAbsolutePosition(self):
        return self.encoder.get_absolute_position().value
