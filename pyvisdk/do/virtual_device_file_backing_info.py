
from pyvisdk.do.virtual_device_backing_info import VirtualDeviceBackingInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDeviceFileBackingInfo(VirtualDeviceBackingInfo):
    '''is a data object type for information about file backing for a device in a virtual
        machine.
    '''
    
    def __init__(self, datastore, fileName):
        # MUST define these
        super(VirtualDeviceFileBackingInfo, self).__init__()
    
        self.data['datastore'] = datastore
        self.data['fileName'] = fileName
    
    
    @property
    def datastore(self):
        '''Reference to the datastore managed object where this file is stored. If the file
        is not located on a datastore, then this reference is null. This is not
        used for configuration.
        '''
        return self.data['datastore']

    @property
    def fileName(self):
        '''Filename for the host file used in this backing.
        '''
        return self.data['fileName']

