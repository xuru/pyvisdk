
================================================================================
HostHyperThreadScheduleInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.host_config_info.HostConfigInfo`,
    :py:class:`~pyvisdk.do.host_cpu_scheduler_system.HostCpuSchedulerSystem`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.host_hyper_thread_schedule_info.HostHyperThreadScheduleInfo
    
    .. py:attribute:: active
    
        The flag to indicate whether or not the CPU scheduler is currently treating hyperthreads as schedulable resources. Setting this property involves a successful invocation of either the enableHyperThreading() method ("true") or the disableHyperthreading() method ("false"). The property is set once the system is rebooted.
        
    
    .. py:attribute:: available
    
        The flag to indicate whether or not hyperthreading optimization is available on the system. This property is set by VMware prior to installation.
        
    
    .. py:attribute:: config
    
        The flag to indicate whether or not the CPU scheduler should treat hyperthreads as schedulable resources the next time the CPU scheduler starts. * This property is set to "true" by successfully invoking the enableHyperThreading() method. * This property is set to "false" by successfully invoking the disableHyperthreading() method.
        
    