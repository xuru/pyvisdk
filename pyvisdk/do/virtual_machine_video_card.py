
from pyvisdk.do.virtual_device import VirtualDevice
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineVideoCard(VirtualDevice):
    '''The VirtualVideoCard data object type represents a video card in a virtual
        machine.
    '''
    
    def __init__(self, enable3DSupport, numDisplays, useAutoDetect, videoRamSizeInKB):
        # MUST define these
        super(VirtualMachineVideoCard, self).__init__()
    
        self.data['enable3DSupport'] = enable3DSupport
        self.data['numDisplays'] = numDisplays
        self.data['useAutoDetect'] = useAutoDetect
        self.data['videoRamSizeInKB'] = videoRamSizeInKB
    
    
    @property
    def enable3DSupport(self):
        '''Flag to indicate whether the virtual video card supports 3D functions. This
        property can only be updated when the virtual machine is powered off.
        '''
        return self.data['enable3DSupport']

    @property
    def numDisplays(self):
        '''Indicates the number of supported monitors. The number of displays X the maximum
        resolution of each display is bounded by the video RAM size of the virtual
        video card. This property can only be updated when the virtual machine is
        powered off.
        '''
        return self.data['numDisplays']

    @property
    def useAutoDetect(self):
        '''Flag to indicate whether the display settings of the host on which the virtual
        machine is running should be used to automatically determine the display
        settings of the virtual machine's video card. This setting takes effect at
        virtual machine power-on time. If this value is set to TRUE, numDisplays
        will be ignored.
        '''
        return self.data['useAutoDetect']

    @property
    def videoRamSizeInKB(self):
        '''The size of the framebuffer for a virtual machine.
        '''
        return self.data['videoRamSizeInKB']

