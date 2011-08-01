
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVirtualNicManager(ExtensibleManagedObject):
    '''The VirtualNicManager managed object describes the special vnic configuration of
        the host.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostVirtualNicManager):
        # MUST define these
        super(HostVirtualNicManager, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def QueryNetConfig(self, nicType):
        '''Get the NetConfig for the specified nicType

        :param nicType: The NicType


        :rtype: VirtualNicManagerNetConfig 

        '''
        
        return self.delegate("QueryNetConfig")(nicType)
        

    def DeselectVnicForNicType(self, device, nicType):
        '''Deselect the VirtualNic to be a special type.

        :param device: The device that uniquely identifies the VirtualNic.

        :param nicType: The type of VirtualNic that would be deselected

        '''
        
        return self.delegate("DeselectVnicForNicType")(device,nicType)
        

    def SelectVnicForNicType(self, device, nicType):
        '''Select the NicType of the VirtualNic. Selecting a device automatically deselects
        the previous selection if NetConfig#multiSelectAllowed is false for the
        specified nicType. Else, the device is added to the list of selected nics.

        :param device: The device that uniquely identifies the VirtualNic.

        :param nicType: The type of VirtualNic that would be selected

        '''
        
        return self.delegate("SelectVnicForNicType")(device,nicType)
        
