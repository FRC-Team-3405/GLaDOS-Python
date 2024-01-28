from phoenix6.signals import InvertedValue,SensorDirectionValue
import math

# Contains values and required settings for common COTS swerve modules.
class COTSTalonFXSwerveConstants:
    def __init__(self, wheelDiameter, angleGearRatio, driveGearRatio, angleKP, angleKI, angleKD, driveMotorInvert, angleMotorInvert, cancoderInvert):
        self.wheelDiameter = wheelDiameter
        self.wheelCircumference = wheelDiameter * math.pi
        self.angleGearRatio = angleGearRatio
        self.driveGearRatio = driveGearRatio
        self.angleKP = angleKP
        self.angleKI = angleKI
        self.angleKD = angleKD
        self.driveMotorInvert = driveMotorInvert
        self.angleMotorInvert = angleMotorInvert
        self.cancoderInvert = cancoderInvert

class WCP:
    class SwerveXStandard:
        def Falcon500(self,driveGearRatio):
            self.wheelDiameter = 4.0 * 0.0254
    
            # (396 / 35) : 1 
            self.angleGearRatio = ((396.0 / 35.0) / 1.0)
    
            self.angleKP = 1.0
            self.angleKI = 0.0
            self.angleKD = 0.0
    
            self.driveMotorInvert = InvertedValue.COUNTER_CLOCKWISE_POSITIVE
            self.angleMotorInvert = InvertedValue.CLOCKWISE_POSITIVE
            self.cancoderInvert = SensorDirectionValue.COUNTER_CLOCKWISE_POSITIVE
            return COTSTalonFXSwerveConstants(self.wheelDiameter, self.angleGearRatio, driveGearRatio, self.angleKP, self.angleKI, self.angleKD, self.driveMotorInvert, self.angleMotorInvert, self.cancoderInvert)
        
        def KrakenX60(driveGearRatio):
            wheelDiameter = 4.0 * 0.0254
    
            # (396 / 35) : 1
            angleGearRatio = ((396.0 / 35.0) / 1.0)
    
            angleKP = 1.0
            angleKI = 0.0
            angleKD = 0.0
    
            driveMotorInvert = InvertedValue.COUNTER_CLOCKWISE_POSITIVE
            angleMotorInvert = InvertedValue.CLOCKWISE_POSITIVE
            cancoderInvert = SensorDirectionValue.COUNTER_CLOCKWISE_POSITIVE
            return COTSTalonFXSwerveConstants(wheelDiameter, angleGearRatio, driveGearRatio, angleKP, angleKI, angleKD, driveMotorInvert, angleMotorInvert, cancoderInvert)

        class driveRatios:
            # WCP SwerveX Standard X1 - 10 Tooth - (7.85 : 1)
            X1_10 = (7.85 / 1.0)
            
            # WCP SwerveX Standard X1 - 11 Tooth - (7.13 : 1)
            X1_11 = (7.13 / 1.0)
            
            # WCP SwerveX Standard X1 - 12 Tooth - (6.54 : 1)
            X1_12 = (6.54 / 1.0)
            
            # WCP SwerveX Standard X2 - 10 Tooth - (6.56 : 1)
            X2_10 = (6.56 / 1.0)
            
            # WCP SwerveX Standard X2 - 11 Tooth - (5.96 : 1)
            X2_11 = (5.96 / 1.0)
            
            # WCP SwerveX Standard X2 - 12 Tooth - (5.46 : 1)
            X2_12 = (5.46 / 1.0)
            
            # WCP SwerveX Standard X3 - 12 Tooth - (5.14 : 1)
            X3_12 = (5.14 / 1.0)
            
            # WCP SwerveX Standard X3 - 13 Tooth - (4.75 : 1)
            X3_13 = (4.75 / 1.0)
            
            # WCP SwerveX Standard X3 - 14 Tooth - (4.41 : 1)
            X3_14 = (4.41 / 1.0)

    # West Coast Products - SwerveX Flippe
    class SwerveXFlipped:
        # West Coast Products - SwerveX Flipped (Falcon 500
        def Falcon500(driveGearRatio):
            wheelDiameter = 4.0 * 0.0254

            # (468 / 35) : 1
            angleGearRatio = ((468.0 / 35.0) / 1.0)

            angleKP = 1.0
            angleKI = 0.0
            angleKD = 0.0

            driveMotorInvert = InvertedValue.COUNTER_CLOCKWISE_POSITIVE
            angleMotorInvert = InvertedValue.CLOCKWISE_POSITIVE
            cancoderInvert = SensorDirectionValue.COUNTER_CLOCKWISE_POSITIVE
            return COTSTalonFXSwerveConstants(wheelDiameter, angleGearRatio, driveGearRatio, angleKP, angleKI, angleKD, driveMotorInvert, angleMotorInvert, cancoderInvert)
        
        # West Coast Products - SwerveX Flipped (Kraken X60
        def KrakenX60(driveGearRatio):
            wheelDiameter = 4.0 * 0.0254

            # (468 / 35) : 1
            angleGearRatio = ((468.0 / 35.0) / 1.0)

            angleKP = 1.0
            angleKI = 0.0
            angleKD = 0.0

            driveMotorInvert = InvertedValue.COUNTER_CLOCKWISE_POSITIVE
            angleMotorInvert = InvertedValue.CLOCKWISE_POSITIVE
            cancoderInvert = SensorDirectionValue.COUNTER_CLOCKWISE_POSITIVE
            return COTSTalonFXSwerveConstants(wheelDiameter, angleGearRatio, driveGearRatio, angleKP, angleKI, angleKD, driveMotorInvert, angleMotorInvert, cancoderInvert)


        class driveRatios:
            # WCP SwerveX Flipped X1 - 10 Tooth - (8.10 : 1)
            X1_10 = (8.10 / 1.0)
            
            # WCP SwerveX Flipped X1 - 11 Tooth - (7.36 : 1)
            X1_11 = (7.36 / 1.0)
            
            # WCP SwerveX Flipped X1 - 12 Tooth - (6.75 : 1)
            X1_12 = (6.75 / 1.0)
            
            # WCP SwerveX Flipped X2 - 10 Tooth - (6.72 : 1)
            X2_10 = (6.72 / 1.0)
            
            # WCP SwerveX Flipped X2 - 11 Tooth - (6.11 : 1)
            X2_11 = (6.11 / 1.0)
            
            # WCP SwerveX Flipped X2 - 12 Tooth - (5.60 : 1)
            X2_12 = (5.60 / 1.0)
            
            # WCP SwerveX Flipped X3 - 10 Tooth - (5.51 : 1)
            X3_10 = (5.51 / 1.0)
            
            # WCP SwerveX Flipped X3 - 11 Tooth - (5.01 : 1)
            X3_11 = (5.01 / 1.0)
            
            # WCP SwerveX Flipped X3 - 12 Tooth - (4.59 : 1)
            X3_12 = (4.59 / 1.0)

# Swerve Drive Specialities
class SDS:
    # Swerve Drive Specialties - MK3 Modul
    class MK3:
        # Swerve Drive Specialties - MK3 Module (Falcon 500
        def Falcon500(driveGearRatio):
            wheelDiameter = 4.0 * 0.0254
    
            # 12.8 : 1
            angleGearRatio = (12.8 / 1.0)
    
            angleKP = 1.0
            angleKI = 0.0
            angleKD = 0.0
    
            driveMotorInvert = InvertedValue.COUNTER_CLOCKWISE_POSITIVE
            angleMotorInvert = InvertedValue.COUNTER_CLOCKWISE_POSITIVE
            cancoderInvert = SensorDirectionValue.COUNTER_CLOCKWISE_POSITIVE
            return COTSTalonFXSwerveConstants(wheelDiameter, angleGearRatio, driveGearRatio, angleKP, angleKI, angleKD, driveMotorInvert, angleMotorInvert, cancoderInvert)
        
        # Swerve Drive Specialties - MK3 Module (Kraken X60
        def KrakenX60(driveGearRatio):
            wheelDiameter = 4.0 * 0.0254
    
            # 12.8 : 1
            angleGearRatio = (12.8 / 1.0)
    
            angleKP = 1.0
            angleKI = 0.0
            angleKD = 0.0
    
            driveMotorInvert = InvertedValue.COUNTER_CLOCKWISE_POSITIVE
            angleMotorInvert = InvertedValue.COUNTER_CLOCKWISE_POSITIVE
            cancoderInvert = SensorDirectionValue.COUNTER_CLOCKWISE_POSITIVE
            return COTSTalonFXSwerveConstants(wheelDiameter, angleGearRatio, driveGearRatio, angleKP, angleKI, angleKD, driveMotorInvert, angleMotorInvert, cancoderInvert)

        class driveRatios:
            # SDS MK3 - (8.16 : 1)
            Standard = (8.16 / 1.0)
            # SDS MK3 - (6.86 : 1)
            Fast = (6.86 / 1.0)

    # Swerve Drive Specialties - MK4 Modul
    class MK4:
        # Swerve Drive Specialties - MK4 Module (Falcon 500
        def Falcon500(driveGearRatio):
            wheelDiameter = 4.0 * 0.0254
    
            # 12.8 : 1
            angleGearRatio = (12.8 / 1.0)
    
            angleKP = 1.0
            angleKI = 0.0
            angleKD = 0.0
    
            driveMotorInvert = InvertedValue.COUNTER_CLOCKWISE_POSITIVE
            angleMotorInvert = InvertedValue.COUNTER_CLOCKWISE_POSITIVE
            cancoderInvert = SensorDirectionValue.COUNTER_CLOCKWISE_POSITIVE
            return COTSTalonFXSwerveConstants(wheelDiameter, angleGearRatio, driveGearRatio, angleKP, angleKI, angleKD, driveMotorInvert, angleMotorInvert, cancoderInvert)

        # Swerve Drive Specialties - MK4 Module (Kraken X60
        def KrakenX60(driveGearRatio):
            wheelDiameter = 4.0 * 0.0254
    
            # 12.8 : 1
            angleGearRatio = (12.8 / 1.0)
    
            angleKP = 1.0
            angleKI = 0.0
            angleKD = 0.0
    
            driveMotorInvert = InvertedValue.COUNTER_CLOCKWISE_POSITIVE
            angleMotorInvert = InvertedValue.COUNTER_CLOCKWISE_POSITIVE
            cancoderInvert = SensorDirectionValue.COUNTER_CLOCKWISE_POSITIVE
            return COTSTalonFXSwerveConstants(wheelDiameter, angleGearRatio, driveGearRatio, angleKP, angleKI, angleKD, driveMotorInvert, angleMotorInvert, cancoderInvert)

        class driveRatios:
            # SDS MK4 - (8.14 : 1)
            L1 = (8.14 / 1.0)
            # SDS MK4 - (6.75 : 1)
            L2 = (6.75 / 1.0)
            # SDS MK4 - (6.12 : 1)
            L3 = (6.12 / 1.0)
            # SDS MK4 - (5.14 : 1)
            L4 = (5.14 / 1.0)


    # Swerve Drive Specialties - MK4i Modul
    class MK4i:
        # Swerve Drive Specialties - MK4i Module (Falcon 500
        def Falcon500(driveGearRatio):
            wheelDiameter = 4.0 * 0.0254
    
            # (150 / 7) : 1
            angleGearRatio = ((150.0 / 7.0) / 1.0)
    
            angleKP = 100.0
            angleKI = 0.0
            angleKD = 0.0
    
            driveMotorInvert = InvertedValue.COUNTER_CLOCKWISE_POSITIVE
            angleMotorInvert = InvertedValue.CLOCKWISE_POSITIVE
            cancoderInvert = SensorDirectionValue.COUNTER_CLOCKWISE_POSITIVE
            return COTSTalonFXSwerveConstants(wheelDiameter, angleGearRatio, driveGearRatio, angleKP, angleKI, angleKD, driveMotorInvert, angleMotorInvert, cancoderInvert)

        # Swerve Drive Specialties - MK4i Module (Kraken X60
        def KrakenX60(driveGearRatio):
            wheelDiameter = 4.0 * 0.0254
    
            # (150 / 7) : 1
            angleGearRatio = ((150.0 / 7.0) / 1.0)
    
            angleKP = 1.0
            angleKI = 0.0
            angleKD = 0.0
    
            driveMotorInvert = InvertedValue.COUNTER_CLOCKWISE_POSITIVE
            angleMotorInvert = InvertedValue.CLOCKWISE_POSITIVE
            cancoderInvert = SensorDirectionValue.COUNTER_CLOCKWISE_POSITIVE
            return COTSTalonFXSwerveConstants(wheelDiameter, angleGearRatio, driveGearRatio, angleKP, angleKI, angleKD, driveMotorInvert, angleMotorInvert, cancoderInvert)
    

        class driveRatios:
            # SDS MK4i - (8.14 : 1)
            L1 = (8.14 / 1.0)
            # SDS MK4i - (6.75 : 1)
            L2 = (6.75 / 1.0)
            # SDS MK4i - (6.12 : 1)
            L3 = (6.12 / 1.0)