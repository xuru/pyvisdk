
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVSFeatureCapability(DynamicData):
    '''Dataobject representing the feature capabilities supported by the vNetwork
        Distributed Virtual Switch.
    '''
    
    def __init__(self, networkResourceManagementSupported, networkResourcePoolHighShareValue, nicTeamingPolicy, vmDirectPathGen2Supported):
        # MUST define these
        super(DVSFeatureCapability, self).__init__()
    
        self.data['networkResourceManagementSupported'] = networkResourceManagementSupported
        self.data['networkResourcePoolHighShareValue'] = networkResourcePoolHighShareValue
        self.data['nicTeamingPolicy'] = nicTeamingPolicy
        self.data['vmDirectPathGen2Supported'] = vmDirectPathGen2Supported
    
    
    @property
    def networkResourceManagementSupported(self):
        '''Flag to indicate whether network I/O control is supported on the vNetwork
        Distributed Switch.
        '''
        return self.data['networkResourceManagementSupported']

    @property
    def networkResourcePoolHighShareValue(self):
        '''This is the value for high in shares. This implicitly defines the legal range of
        share values to be between 1 and this. This also defines values for other
        level types, such as normal being one half of this value and low being one
        fourth of this value.
        '''
        return self.data['networkResourcePoolHighShareValue']

    @property
    def nicTeamingPolicy(self):
        '''The available teaming modes for the vNetwork Distributed Switch. The value can be
        one or more of DistributedVirtualSwitchNicTeamingPolicyMode.
        '''
        return self.data['nicTeamingPolicy']

    @property
    def vmDirectPathGen2Supported(self):
        '''Flag to indicate whether VMDirectPath Gen 2 is supported on the vNetwork
        Distributed Switch.
        '''
        return self.data['vmDirectPathGen2Supported']

