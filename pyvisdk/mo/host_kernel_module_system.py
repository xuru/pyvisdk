
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostKernelModuleSystem(BaseEntity):
    '''The KernelModuleSystem managed object controls the configuration of kernel modules
        on the host.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostKernelModuleSystem):
        # MUST define these
        super(HostKernelModuleSystem, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def QueryConfiguredModuleOptionString(self, name, options):
        '''Query the options configured to be passed to the kernel module when loaded. Note
        that this is not necessarily the option string currently in use by the
        kernel module.

        :param name: Module name.

        :param options: Option string to be passed to the kernel module at load time.

        '''
        
        return self.delegate("QueryConfiguredModuleOptionString")(name,options)
        

    def QueryModules(self, name, options):
        '''Query the set of modules on the host.

        :param name: Module name.

        :param options: Option string to be passed to the kernel module at load time.

        '''
        
        return self.delegate("QueryModules")(name,options)
        

    def UpdateModuleOptionString(self, name, options):
        '''Specifies the options to be passed to the kernel module when loaded.

        :param name: Module name.

        :param options: Option string to be passed to the kernel module at load time.

        '''
        
        return self.delegate("UpdateModuleOptionString")(name,options)
        
