
==================================================================================================
HostNumericSensorHealthState
==================================================================================================

.. describe:: HostNumericSensorHealthState

    Health state of the numeric sensor as reported by the sensor probes.
    
    
    .. py:data:: HostNumericSensorHealthState.green
    
        The sensor is operating under normal conditions
        
    
    .. py:data:: HostNumericSensorHealthState.red
    
        The sensor is operating under critical or fatal conditions. This may directly affect the functioning of both the sensor and related components.
        
    
    .. py:data:: HostNumericSensorHealthState.unknown
    
        The implementation cannot report on the current health state of the physical element
        
    
    .. py:data:: HostNumericSensorHealthState.yellow
    
        The sensor is operating under conditions that are non-critical.
        
    