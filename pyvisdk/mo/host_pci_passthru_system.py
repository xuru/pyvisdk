
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPciPassthruSystem(ExtensibleManagedObject):
    '''This managed object manages the PciPassthru state of the host.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostPciPassthruSystem):
        # MUST define these
        super(HostPciPassthruSystem, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def pciPassthruInfo(self):
        '''
        Array of PciPassthru information
        '''
        return self.update('pciPassthruInfo')


    def UpdatePassthruConfig(self, config):
        '''Updates the PciPassthru configuration, this will get called for the dependent
        device with the enabled bool set

        :param config: The new PciPassthru configuration information.

        '''
        
        return self.delegate("UpdatePassthruConfig")(config)
        

    def Refresh(self):
        '''Refresh the available PciPassthru information.
        '''
        
        return self.delegate("Refresh")()
        
