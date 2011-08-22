
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVirtualNicManager(ExtensibleManagedObject):
    '''The VirtualNicManager managed object describes the special vnic configuration
    of the host.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostVirtualNicManager):
        super(HostVirtualNicManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def info(self):
        '''Network configuration.'''
        return self.update('info')
    
    
    
    def DeselectVnicForNicType(self):
        '''Deselect the VirtualNic to be a special type.
        :rtype: None
        :returns: 
        '''
        return self.delegate("DeselectVnicForNicType")()
    
    def QueryNetConfig(self):
        '''Get the NetConfig for the specified nicType
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryNetConfig")()
    
    def SelectVnicForNicType(self):
        '''Select the NicType of the VirtualNic. Selecting a device automatically
        deselects the previous selection if NetConfig#multiSelectAllowed is false for
        the specified nicType. Else, the device is added to the list of selected nics.
        :rtype: None
        :returns: 
        '''
        return self.delegate("SelectVnicForNicType")()