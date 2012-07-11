
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPciPassthruSystem(ExtensibleManagedObject):
    '''This managed object manages the PciPassthru state of the host.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostPciPassthruSystem):
        super(HostPciPassthruSystem, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def pciPassthruInfo(self):
        '''Array of PciPassthru information'''
        return self.update('pciPassthruInfo')

    
    
    def Refresh(self):
        '''Refresh the available PciPassthru information.
        
        '''
        return self.delegate("Refresh")()
    
    def UpdatePassthruConfig(self, config):
        '''Updates the PciPassthru configuration, this will get called for the dependent
        device with the enabled bool set
        
        :param config: The new PciPassthru configuration information.
        
        '''
        return self.delegate("UpdatePassthruConfig")(config)