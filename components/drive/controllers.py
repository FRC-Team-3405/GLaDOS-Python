class Ps4_controller():
    def __init__(self) -> None:
        self.ButtonMap = {"ShiftUp": 6,
                          "ShiftDown": 5,
                          "SpeedUp": 7,
                          "SpeedDown": 8,
                          "FullForward": 4,
                          "FullBackward": 1}
        self.AxisMap = {"RightY": 5,
                        "RightX": 2,
                        "LeftY": 1,
                        "LeftX": 0}
        
class Xbox_controller():
    def __init__(self) -> None:
        self.ButtonMap = {"Center": 2,
                          "ShiftDown": 5,
                          "SpeedUp": 7,
                          "SpeedDown": 8,
                          "Centric": 4,
                          "FullBackward": 1}
        self.AxisMap = {"RightY": 5,
                        "RightX": 4,
                        "LeftY": 1,
                        "LeftX": 0}