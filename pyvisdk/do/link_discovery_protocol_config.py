
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LinkDiscoveryProtocolConfig(DynamicData):
    '''Dataobject representing the link discovery protocol configuration for a virtual or
        distributed virtual switch.
    '''
    
    def __init__(self, operation, protocol):
        # MUST define these
        super(LinkDiscoveryProtocolConfig, self).__init__()
    
        self.data['operation'] = operation
        self.data['protocol'] = protocol
    
    
    @property
    def operation(self):
        '''Whether to advertise or listen. For valid values see
        LinkDiscoveryProtocolConfigOperationType.
        '''
        return self.data['operation']

    @property
    def protocol(self):
        '''The discovery protocol type. For valid values see
        LinkDiscoveryProtocolConfigProtocolType.
        '''
        return self.data['protocol']

