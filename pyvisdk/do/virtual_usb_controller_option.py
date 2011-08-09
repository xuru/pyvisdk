
from pyvisdk.do.virtual_controller_option import VirtualControllerOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualUSBControllerOption(VirtualControllerOption):
    '''The VirtualUSBControllerOption data object type contains the options for a virtual
        USB Host Controller Interface.
    '''
    
    def __init__(self, autoConnectDevices, ehciSupported):
        # MUST define these
        super(VirtualUSBControllerOption, self).__init__()
    
        self.data['autoConnectDevices'] = autoConnectDevices
        self.data['ehciSupported'] = ehciSupported
    
    
    @property
    def autoConnectDevices(self):
        '''Flag to indicate whether or not the ability to autoconnect devices is enabled for
        this virtual USB controller.
        '''
        return self.data['autoConnectDevices']

    @property
    def ehciSupported(self):
        '''Flag to indicate whether or not enhanced host controller interface (USB 2.0) is
        available on this virtual USB controller.
        '''
        return self.data['ehciSupported']

