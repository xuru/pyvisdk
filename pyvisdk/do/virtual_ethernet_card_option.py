
from pyvisdk.do.virtual_device_option import VirtualDeviceOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualEthernetCardOption(VirtualDeviceOption):
    '''This data object type contains the options for the virtual ethernet card data
        object type.
    '''
    
    def __init__(self, macType, supportedOUI):
        # MUST define these
        super(VirtualEthernetCardOption, self).__init__()
    
        self.data['macType'] = macType
        self.data['supportedOUI'] = supportedOUI
    
    
    @property
    def macType(self):
        '''The supported MAC address types.
        '''
        return self.data['macType']

    @property
    def supportedOUI(self):
        '''The valid Organizational Unique Identifiers (OUIs) supported by this virtual
        Ethernet card.
        '''
        return self.data['supportedOUI']

