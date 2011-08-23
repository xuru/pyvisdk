
================================================================================
HostNumericSensorInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_system_health_info.HostSystemHealthInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.element_description.ElementDescription`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_numeric_sensor_info.HostNumericSensorInfo
    
    .. py:attribute:: baseUnits
    
        The base units in which the sensor reading is specified. If rateUnits is set the units of the current reading is further qualified by the rateUnits.
        
    
    .. py:attribute:: currentReading
    
        The current reading of the element indicated by the sensor. The actual sensor reading is obtained by multiplying the current reading by the scale factor.
        
    
    .. py:attribute:: healthState
    
        The health state of the of the element indicated by the sensor. This property is populated only for sensors that support threshold settings.
        
    
    .. py:attribute:: name
    
        The name of the physical element associated with the sensor
        
    
    .. py:attribute:: rateUnits
    
        The rate units in which the sensor reading is specified. For example if the baseUnits is Volts and the rateUnits is per second the value returned by the sensor are in Volts/second.
        
    
    .. py:attribute:: sensorType
    
        The type of the sensor. If the sensor type is set to Other the sensor name can be used to further identify the type of sensor. The sensor units can also be used to further implicitly determine the type of the sensor.
        
    
    .. py:attribute:: unitModifier
    
        The unit multiplier for the values returned by the sensor. All values returned by the sensor are current reading * 10 raised to the power of the UnitModifier.
        
    