
================================================================================
DVSTrafficShapingPolicy
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.dv_port_setting.DVPortSetting`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.bool_policy.BoolPolicy`,
    :py:class:`~pyvisdk.do.long_policy.LongPolicy`
    
.. describe:: Since
    
    vSphere API 4.0
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.inheritable_policy.InheritablePolicy`
    
.. class:: pyvisdk.do.dvs_traffic_shaping_policy.DVSTrafficShapingPolicy
    
    .. py:attribute:: averageBandwidth
    
        The average bandwidth in bits per second if shaping is enabled on the port.
        
    
    .. py:attribute:: burstSize
    
        The maximum burst size allowed in bytes if shaping is enabled on the port.
        
    
    .. py:attribute:: enabled
    
        The flag to indicate whether or not traffic shaper is enabled on the port.
        
    
    .. py:attribute:: peakBandwidth
    
        The peak bandwidth during bursts in bits per second if traffic shaping is enabled on the port.
        
    