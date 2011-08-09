
from pyvisdk.do.virtual_device_remote_device_backing_option import VirtualDeviceRemoteDeviceBackingOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualCdromRemotePassthroughBackingOption(VirtualDeviceRemoteDeviceBackingOption):
    '''The VirtualCdromOption.RemotePassthroughBackingOption data object type contains
        the options for a remote pass-through CD-ROM device backing.Note that the
        server cannot present a list of valid remote backing devices because it is
        unable to scan remote hosts.
    '''
    
    def __init__(self, exclusive):
        # MUST define these
        super(VirtualCdromRemotePassthroughBackingOption, self).__init__()
    
        self.data['exclusive'] = exclusive
    
    
    @property
    def exclusive(self):
        '''Flag to indicate whether or not exclusive CD-ROM device access is supported.
        '''
        return self.data['exclusive']

