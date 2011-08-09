
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostSnmpConfigSpec(DynamicData):
    '''
    '''
    
    def __init__(self, enabled, port, readOnlyCommunities, trapTargets):
        # MUST define these
        super(HostSnmpConfigSpec, self).__init__()
    
        self.data['enabled'] = enabled
        self.data['port'] = port
        self.data['readOnlyCommunities'] = readOnlyCommunities
        self.data['trapTargets'] = trapTargets
    
    
    @property
    def enabled(self):
        '''
        '''
        return self.data['enabled']

    @property
    def port(self):
        '''
        '''
        return self.data['port']

    @property
    def readOnlyCommunities(self):
        '''
        '''
        return self.data['readOnlyCommunities']

    @property
    def trapTargets(self):
        '''
        '''
        return self.data['trapTargets']

