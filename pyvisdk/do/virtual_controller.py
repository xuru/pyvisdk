
from pyvisdk.do.virtual_device import VirtualDevice
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualController(VirtualDevice):
    '''VirtualController is the base data object type for a device controller in a
        virtual machine. VirtualController extends VirtualDevice to inherit
        general information about a controller (such as name and description), and
        to allow controllers to appear in a generic list of virtual devices.
    '''
    
    def __init__(self, busNumber, device):
        # MUST define these
        super(VirtualController, self).__init__()
    
        self.data['busNumber'] = busNumber
        self.data['device'] = device
    
    
    @property
    def busNumber(self):
        '''Bus number associated with this controller.
        '''
        return self.data['busNumber']

    @property
    def device(self):
        '''List of devices currently controlled by this controller. Each entry contains the
        key property of the corresponding device object.
        '''
        return self.data['device']

