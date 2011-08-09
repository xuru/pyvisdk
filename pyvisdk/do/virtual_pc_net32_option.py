
from pyvisdk.do.virtual_ethernet_card_option import VirtualEthernetCardOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualPCNet32Option(VirtualEthernetCardOption):
    '''The VirtualPCNet32Option data object type defines the options for the
        VirtualPCNet32 data object type. Except for the boolean supportsMorphing
        option, the options are inherited from the VirtualEthernetCardOption data
        object type.
    '''
    
    def __init__(self, supportsMorphing):
        # MUST define these
        super(VirtualPCNet32Option, self).__init__()
    
        self.data['supportsMorphing'] = supportsMorphing
    
    
    @property
    def supportsMorphing(self):
        '''Indicates that this Ethernet card supports morphing into vmxnet when appropriate.
        This means that, if supportsMorphing="true", the virtual AMD Lance PCNet32
        Ethernet card becomes a vmxnet Ethernet card with its added performance
        capabilities when appropriate.
        '''
        return self.data['supportsMorphing']

