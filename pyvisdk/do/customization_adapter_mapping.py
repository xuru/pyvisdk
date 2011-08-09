
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationAdapterMapping(DynamicData):
    '''Data object type to associate a virtual network adapter with its IP settings.
    '''
    
    def __init__(self, adapter, macAddress):
        # MUST define these
        super(CustomizationAdapterMapping, self).__init__()
    
        self.data['adapter'] = adapter
        self.data['macAddress'] = macAddress
    
    
    @property
    def adapter(self):
        '''The IP settings for the associated virtual network adapter.
        '''
        return self.data['adapter']

    @property
    def macAddress(self):
        '''The MAC address of a network adapter being customized. The client cannot change
        this value because the guest operating system has no control over the MAC
        address of a virtual network adapter.
        '''
        return self.data['macAddress']

