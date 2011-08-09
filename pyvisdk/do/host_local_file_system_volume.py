
from pyvisdk.do.host_file_system_volume import HostFileSystemVolume
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostLocalFileSystemVolume(HostFileSystemVolume):
    '''Local file system volume.
    '''
    
    def __init__(self, device):
        # MUST define these
        super(HostLocalFileSystemVolume, self).__init__()
    
        self.data['device'] = device
    
    
    @property
    def device(self):
        '''The device of the local file system.
        '''
        return self.data['device']

