
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostSnmpSystemAgentLimits(DynamicData):
    '''
    '''
    
    def __init__(self, capability, maxBufferSize, maxCommunityLength, maxReadOnlyCommunities, maxTrapDestinations):
        # MUST define these
        super(HostSnmpSystemAgentLimits, self).__init__()
    
        self.data['capability'] = capability
        self.data['maxBufferSize'] = maxBufferSize
        self.data['maxCommunityLength'] = maxCommunityLength
        self.data['maxReadOnlyCommunities'] = maxReadOnlyCommunities
        self.data['maxTrapDestinations'] = maxTrapDestinations
    
    
    @property
    def capability(self):
        '''Supported Capability for this agent
        '''
        return self.data['capability']

    @property
    def maxBufferSize(self):
        '''SNMP input buffer size
        '''
        return self.data['maxBufferSize']

    @property
    def maxCommunityLength(self):
        '''Max length of community
        '''
        return self.data['maxCommunityLength']

    @property
    def maxReadOnlyCommunities(self):
        '''number of allowed communities
        '''
        return self.data['maxReadOnlyCommunities']

    @property
    def maxTrapDestinations(self):
        '''number of allowed destinations for notifications
        '''
        return self.data['maxTrapDestinations']

