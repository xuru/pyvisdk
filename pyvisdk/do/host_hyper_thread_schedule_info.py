
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostHyperThreadScheduleInfo(DynamicData):
    '''This data object type describes the CpuSchedulerSystem configuration for
        optimizing hyperthreading. The primary hyperthreading optimization
        employed by the CpuSchedulerSystem is to utilize hyperthreads as
        additional schedulable resources. Although hyperthreads provide limited
        additional concurrency, certain workloads (such as idling) can take
        advantage of these hyperthreads. This is particularly useful for SMP
        virtual machines that use gang scheduling. (Gang scheduling refers to a
        situation in which all of a parallel program's tasks are grouped into a
        "gang" and concurrently scheduled on distinct processors of a parallel
        computer system.)Changes to the hyperthreading optimization can take
        effect only after a system restart. Therefore, while it is possible to
        change the configuration at any time, the change will take effect only on
        the next boot.
    '''
    
    def __init__(self, active, available, config):
        # MUST define these
        super(HostHyperThreadScheduleInfo, self).__init__()
    
        self.data['active'] = active
        self.data['available'] = available
        self.data['config'] = config
    
    
    @property
    def active(self):
        '''The flag to indicate whether or not the CPU scheduler is currently treating
        hyperthreads as schedulable resources. Setting this property involves a
        successful invocation of either the enableHyperThreading() method ("true")
        or the disableHyperthreading() method ("false"). The property is set once
        the system is rebooted.
        '''
        return self.data['active']

    @property
    def available(self):
        '''The flag to indicate whether or not hyperthreading optimization is available on
        the system. This property is set by VMware prior to installation.
        '''
        return self.data['available']

    @property
    def config(self):
        '''The flag to indicate whether or not the CPU scheduler should treat hyperthreads as
        schedulable resources the next time the CPU scheduler starts. * This
        property is set to "true" by successfully invoking the
        enableHyperThreading() method. * This property is set to "false" by
        successfully invoking the disableHyperthreading() method.
        '''
        return self.data['config']

