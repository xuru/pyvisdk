
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DvsOutOfSyncHostArgument(DynamicData):
    '''The host on which the DVS configuration is different from that of Virtual Center
        server.
    '''
    
    def __init__(self, configParamters, outOfSyncHost):
        # MUST define these
        super(DvsOutOfSyncHostArgument, self).__init__()
    
        self.data['configParamters'] = configParamters
        self.data['outOfSyncHost'] = outOfSyncHost
    
    
    @property
    def configParamters(self):
        '''The DVS configuration parameters that are different between Virtual Center server
        and the host.
        '''
        return self.data['configParamters']

    @property
    def outOfSyncHost(self):
        '''The host.
        '''
        return self.data['outOfSyncHost']

