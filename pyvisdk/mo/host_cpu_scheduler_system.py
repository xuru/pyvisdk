
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostCpuSchedulerSystem(ExtensibleManagedObject):
    '''This managed object provides an interface through which you can gather and
    configure the host CPU scheduler policies that affect the performance of
    running virtual machines.: This managed object is useful only on platforms
    where resource management controls are available to optimize the running of
    virtual machines.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostCpuSchedulerSystem):
        super(HostCpuSchedulerSystem, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def hyperthreadInfo(self):
        '''The hyperthread configuration for the CpuSchedulerSystem. The existence of this
        data object type indicates if the CPU scheduler is capable of scheduling
        hyperthreads as resources.'''
        return self.update('hyperthreadInfo')

    
    
    def DisableHyperThreading(self):
        '''Don't treat hyperthreads as schedulable resources the next time the CPU
        scheduler starts. If successful, this operation will change the configured
        setting.
        
        '''
        return self.delegate("DisableHyperThreading")()
    
    def EnableHyperThreading(self):
        '''Treat hyperthreads as schedulable resources the next time the CPU scheduler
        starts. If successful, this operation will set the config property to "true".
        
        '''
        return self.delegate("EnableHyperThreading")()