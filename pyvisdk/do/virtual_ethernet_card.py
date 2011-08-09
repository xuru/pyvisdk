
from pyvisdk.do.virtual_device import VirtualDevice
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualEthernetCard(VirtualDevice):
    '''This data object type contains the properties of an Ethernet adapter attached to a
        virtual machine.
    '''
    
    def __init__(self, addressType):
        # MUST define these
        super(VirtualEthernetCard, self).__init__()
    
        self.data['addressType'] = addressType
    
    
    @property
    def addressType(self):
        '''MAC address type.
        '''
        return self.data['addressType']

