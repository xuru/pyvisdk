
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class IpPoolAssociation(DynamicData):
    '''Information about a network or portgroup that is associated to an IP pool.
    '''
    
    def __init__(self, network, networkName):
        # MUST define these
        super(IpPoolAssociation, self).__init__()
    
        self.data['network'] = network
        self.data['networkName'] = networkName
    
    
    @property
    def network(self):
        '''The network object
        '''
        return self.data['network']

    @property
    def networkName(self):
        '''The name of the network or portgroup
        '''
        return self.data['networkName']

