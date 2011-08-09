
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostConnectInfoNetworkInfo(DynamicData):
    '''The base data object type for information about networks on the host.
    '''
    
    def __init__(self, summary):
        # MUST define these
        super(HostConnectInfoNetworkInfo, self).__init__()
    
        self.data['summary'] = summary
    
    
    @property
    def summary(self):
        '''Basic network information, such as network name. The managed object reference is
        not set.
        '''
        return self.data['summary']

