
from pyvisdk.do.virtual_device_device_backing_option import VirtualDeviceDeviceBackingOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualCdromPassthroughBackingOption(VirtualDeviceDeviceBackingOption):
    '''The VirtualCdromOption.PassthroughBackingOption data object type contains the
        options for a pass-through CD-ROM device backing.
    '''
    
    def __init__(self, exclusive):
        # MUST define these
        super(VirtualCdromPassthroughBackingOption, self).__init__()
    
        self.data['exclusive'] = exclusive
    
    
    @property
    def exclusive(self):
        '''Flag to indicate whether or not exclusive CD-ROM device access is supported.
        '''
        return self.data['exclusive']

