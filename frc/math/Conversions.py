class Conversions():
    def RPSToMPS(self,wheelRPS,circumference):
        """Returns Wheel Velocity: (in Rotations per Second)"""
        return wheelRPS * circumference
    
    def MPSToRPS(self,wheelMPS,circumference):
        """Wheel Distance: (in Meters)"""
        return wheelMPS / circumference
    
    def rotationsToMeters(wheelRotations, circumference):
        """Wheel Position: (in Rotations)"""
        return wheelRotations * circumference
    
    def metersToRotations(wheelMeters,circumference):
        return wheelMeters / circumference