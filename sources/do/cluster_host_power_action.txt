
================================================================================
ClusterHostPowerAction
================================================================================


.. describe:: See also
    
    :py:class:`~pyvisdk.do.host_power_operation_type.HostPowerOperationType`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.cluster_action.ClusterAction`
    
.. class:: pyvisdk.do.cluster_host_power_action.ClusterHostPowerAction
    
    .. py:attribute:: cpuCapacityMHz
    
        CPU capacity of the host in units of MHz. In case of power-on action, this is the projected increase in the cluster's CPU capacity. In case of power off, this is the projected decrease in the cluster's CPU capacity.
        
    
    .. py:attribute:: memCapacityMB
    
        Memory capacity of the host in units of MM. In case of power-on action, this is the projected increase in the cluster's memory capacity. In case of power off, this is the projected decrease in the cluster's memory capacity.
        
    
    .. py:attribute:: operationType
    
        Specify whether the action is power on or power off
        
    
    .. py:attribute:: powerConsumptionWatt
    
        Estimated power consumption of the host. In case of power-on, this is the projected increase in the cluster's power consumption. In case of power off, this is the projected decrease in the cluster's power consumption
        
    