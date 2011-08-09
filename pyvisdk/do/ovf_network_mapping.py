
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OvfNetworkMapping(DynamicData):
    '''A NetworkMapping is a choice made by the caller about which VI network to use for
        a specific network in the OVF descriptor.
    '''
    
    def __init__(self, name, network):
        # MUST define these
        super(OvfNetworkMapping, self).__init__()
    
        self.data['name'] = name
        self.data['network'] = network
    
    
    @property
    def name(self):
        '''
        '''
        return self.data['name']

    @property
    def network(self):
        '''
        '''
        return self.data['network']

