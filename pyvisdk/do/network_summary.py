
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NetworkSummary(DynamicData):
    '''General information about a network.
    '''
    
    def __init__(self, accessible, ipPoolName, name, network):
        # MUST define these
        super(NetworkSummary, self).__init__()
    
        self.data['accessible'] = accessible
        self.data['ipPoolName'] = ipPoolName
        self.data['name'] = name
        self.data['network'] = network
    
    
    @property
    def accessible(self):
        '''At least one host is configured to provide this network.
        '''
        return self.data['accessible']

    @property
    def ipPoolName(self):
        '''Name of the associated IP pool. Empty if the network is not associated with an IP
        pool.
        '''
        return self.data['ipPoolName']

    @property
    def name(self):
        '''Name of the network.
        '''
        return self.data['name']

    @property
    def network(self):
        '''Reference to the associated managed object.
        '''
        return self.data['network']

