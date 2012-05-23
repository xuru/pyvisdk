
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVirtualNicManager(ExtensibleManagedObject):
    '''The VirtualNicManager managed object describes the special Virtual NIC
    configuration of the host.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostVirtualNicManager):
        super(HostVirtualNicManager, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def info(self):
        '''Network configuration.'''
        return self.update('info')

    
    
    def DeselectVnicForNicType(self, nicType, device):
        '''Deselect the VirtualNic to be a special type.
        
        :param nicType: The type of VirtualNic that would be deselected
        
        :param device: The device that uniquely identifies the VirtualNic.
        
        '''
        return self.delegate("DeselectVnicForNicType")(nicType, device)
    
    def QueryNetConfig(self, nicType):
        '''Get the NetConfig for the specified nicType
        
        :param nicType: The NicType
        
        '''
        return self.delegate("QueryNetConfig")(nicType)
    
    def SelectVnicForNicType(self, nicType, device):
        '''Select the NicType of the VirtualNic. Selecting a device automatically
        deselects the previous selection if NetConfig#multiSelectAllowed is false for
        the specified nicType. Else, the device is added to the list of selected nics.
        
        :param nicType: The type of VirtualNic that would be selected
        
        :param device: The device that uniquely identifies the VirtualNic.
        
        '''
        return self.delegate("SelectVnicForNicType")(nicType, device)