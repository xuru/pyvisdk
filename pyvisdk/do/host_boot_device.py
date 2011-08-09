
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostBootDevice(DynamicData):
    '''The HostBootDevice data object represents a boot device on the host system.
    '''
    
    def __init__(self, description, key):
        # MUST define these
        super(HostBootDevice, self).__init__()
    
        self.data['description'] = description
        self.data['key'] = key
    
    
    @property
    def description(self):
        '''The description of the boot device.
        '''
        return self.data['description']

    @property
    def key(self):
        '''The identifier for the boot device.
        '''
        return self.data['key']

