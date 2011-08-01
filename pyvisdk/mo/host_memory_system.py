
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostMemorySystem(ExtensibleManagedObject):
    '''The MemoryManagerSystem managed object provides an interface through which the
        host memory management policies that affect the performance of running
        virtual machines can be gathered and configured.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostMemorySystem):
        # MUST define these
        super(HostMemorySystem, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def ReconfigureServiceConsoleReservation(self, cfgBytes):
        '''Sets the configured service console memory reservation. This change affects only
        the serviceConsoleReservedCfg property. The configuration change
        propagates to the other properties after the next boot.

        :param cfgBytes: 

        '''
        
        return self.delegate("ReconfigureServiceConsoleReservation")(cfgBytes)
        

    def ReconfigureVirtualMachineReservation(self, spec):
        '''Updates the virtual machine reservation information.

        :param spec: 

        '''
        
        return self.delegate("ReconfigureVirtualMachineReservation")(spec)
        
