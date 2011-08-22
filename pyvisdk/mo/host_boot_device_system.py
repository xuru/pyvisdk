
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostBootDeviceSystem(BaseEntity):
    '''The HostBootDeviceSystem managed object provides methods to query and update a
    host boot device configuration.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostBootDeviceSystem):
        super(HostBootDeviceSystem, self).__init__(core, name=name, ref=ref, type=type)
    
    
    
    
    
    def QueryBootDevices(self):
        '''Retrieves a list of the available boot devices for the host system.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryBootDevices")()
    
    def UpdateBootDevice(self):
        '''Sets the current boot device for the host system.
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdateBootDevice")()