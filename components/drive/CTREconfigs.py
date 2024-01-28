from components.drive.config import *
from phoenix6.configs import *

class CTREConfigs():
    swerveDriveFXConfig = TalonFXConfiguration()
    swerveAngleFXConfig = TalonFXConfiguration()
    swerveCANcoderConfig = CANcoderConfiguration()

    swerveCANcoderConfig.magnet_sensor.sensor_direction = Swerve_constants.canCoderInvert

    swerveAngleFXConfig.motor_output.inverted = Swerve_constants.angleMotorInvert
    swerveAngleFXConfig.motor_output.neutral_mode = Swerve_constants.angleNeutralMode

    # Gear Ratio and Wrapping Config 
    swerveAngleFXConfig.feedback.sensor_to_mechanism_ratio = Swerve_constants.angleGearRatio
    swerveAngleFXConfig.closed_loop_general.continuous_wrap = True
    
    # Current Limiting 
    swerveAngleFXConfig.current_limits.supply_current_limit_enable = Swerve_constants.angleEnableCurrentLimit
    swerveAngleFXConfig.current_limits.supply_current_limit = Swerve_constants.angleCurrentLimit
    swerveAngleFXConfig.current_limits.supply_current_threshold = Swerve_constants.angleCurrentThreshold
    swerveAngleFXConfig.current_limits.supply_time_threshold = Swerve_constants.angleCurrentThresholdTime

    # PID Config 
    swerveAngleFXConfig.slot0.k_p = Swerve_constants.angleKP
    swerveAngleFXConfig.slot0.k_i = Swerve_constants.angleKI
    swerveAngleFXConfig.slot0.k_d = Swerve_constants.angleKD

    #* Swerve Drive Motor Configuration 
    # Motor Inverts and Neutral Mode 
    swerveDriveFXConfig.motor_output.inverted = Swerve_constants.driveMotorInvert
    swerveDriveFXConfig.motor_output.neutral_mode = Swerve_constants.driveNeutralMode

    # Gear Ratio Config 
    swerveDriveFXConfig.feedback.sensor_to_mechanism_ratio = Swerve_constants.driveGearRatio

    # Current Limiting 
    swerveDriveFXConfig.current_limits.supply_current_limit_enable = Swerve_constants.driveEnableCurrentLimit
    swerveDriveFXConfig.current_limits.supply_current_limit = Swerve_constants.driveCurrentLimit
    swerveDriveFXConfig.current_limits.supply_current_threshold = Swerve_constants.driveCurrentThreshold
    swerveDriveFXConfig.current_limits.supply_time_threshold = Swerve_constants.driveCurrentThresholdTime

    # PID Config 
    swerveDriveFXConfig.slot0.k_p = Swerve_constants.driveKP
    swerveDriveFXConfig.slot0.k_i = Swerve_constants.driveKI
    swerveDriveFXConfig.slot0.k_d = Swerve_constants.driveKD

    # Open and Closed Loop Ramping 
    swerveDriveFXConfig.open_loop_ramps.duty_cycle_open_loop_ramp_period = Swerve_constants.openLoopRamp
    swerveDriveFXConfig.open_loop_ramps.voltage_open_loop_ramp_period = Swerve_constants.openLoopRamp

    swerveDriveFXConfig.closed_loop_ramps.duty_cycle_closed_loop_ramp_period = Swerve_constants.closedLoopRamp
    swerveDriveFXConfig.closed_loop_ramps.voltage_closed_loop_ramp_period = Swerve_constants.closedLoopRamp