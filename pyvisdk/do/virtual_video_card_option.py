
from pyvisdk.do.virtual_device_option import VirtualDeviceOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualVideoCardOption(VirtualDeviceOption):
    '''This data object type contains the options for the VirtualVideoCard data object
        type.
    '''
    
    def __init__(self, numDisplays, support3D, useAutoDetect, videoRamSizeInKB):
        # MUST define these
        super(VirtualVideoCardOption, self).__init__()
    
        self.data['numDisplays'] = numDisplays
        self.data['support3D'] = support3D
        self.data['useAutoDetect'] = useAutoDetect
        self.data['videoRamSizeInKB'] = videoRamSizeInKB
    
    
    @property
    def numDisplays(self):
        '''Minimum, maximum and default value for the number of displays.
        '''
        return self.data['numDisplays']

    @property
    def support3D(self):
        '''Flag to indicate whether the virtual video card supports 3D functions.
        '''
        return self.data['support3D']

    @property
    def useAutoDetect(self):
        '''Flag to indicate whether the display settings of the host should be used to
        automatically determine the display settings of the virtual machine's
        video card.
        '''
        return self.data['useAutoDetect']

    @property
    def videoRamSizeInKB(self):
        '''Minimum, maximum and default size of the video frame buffer.
        '''
        return self.data['videoRamSizeInKB']

