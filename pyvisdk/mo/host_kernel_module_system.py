
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostKernelModuleSystem(BaseEntity):
    '''The KernelModuleSystem managed object controls the configuration of kernel
    modules on the host.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostKernelModuleSystem):
        super(HostKernelModuleSystem, self).__init__(core, name=name, ref=ref, type=type)
    
    
    
    
    
    def QueryConfiguredModuleOptionString(self):
        '''Query the options configured to be passed to the kernel module when loaded.
        Note that this is not necessarily the option string currently in use by the
        kernel module.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryConfiguredModuleOptionString")()
    
    def QueryModules(self):
        '''Query the set of modules on the host.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryModules")()
    
    def UpdateModuleOptionString(self):
        '''Specifies the options to be passed to the kernel module when loaded.
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdateModuleOptionString")()