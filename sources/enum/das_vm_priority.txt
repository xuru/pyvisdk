
==================================================================================================
DasVmPriority
==================================================================================================

.. describe:: DasVmPriority

    The priority of the virtual machine determines the preference given to it if sufficient capacity is not available to power on all failed virtual machines. For example, high priority virtual machines on a host get preference over low priority virtual machines.
    
    
    .. py:data:: DasVmPriority.disabled
    
        VMware HA is disabled for this virtual machine.
        
    
    .. py:data:: DasVmPriority.high
    
        Virtual machines with this priority have a higher chance of powering on after a failure if there is insufficient capacity on hosts to meet all virtual machine needs.
        
    
    .. py:data:: DasVmPriority.low
    
        Virtual machines with this priority have a lower chance of powering on after a failure if there is insufficient capacity on hosts to meet all virtual machine needs.
        
    
    .. py:data:: DasVmPriority.medium
    
        Virtual machines with this priority have an intermediate chance of powering on after a failure if there is insufficient capacity on hosts to meet all virtual machine needs.
        
    