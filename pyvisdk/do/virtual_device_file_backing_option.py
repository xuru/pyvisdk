
from pyvisdk.do.virtual_device_backing_option import VirtualDeviceBackingOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDeviceFileBackingOption(VirtualDeviceBackingOption):
    '''The FileBackingOption data class contains file-specific backing options.
    '''
    
    def __init__(self, fileNameExtensions):
        # MUST define these
        super(VirtualDeviceFileBackingOption, self).__init__()
    
        self.data['fileNameExtensions'] = fileNameExtensions
    
    
    @property
    def fileNameExtensions(self):
        '''Valid filename extension for the filename. If no extensions are present, any file
        extension is acceptable.
        '''
        return self.data['fileNameExtensions']

