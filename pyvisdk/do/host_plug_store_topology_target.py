
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPlugStoreTopologyTarget(DynamicData):
    '''This data object represents target information.
    '''
    
    def __init__(self, key, transport):
        # MUST define these
        super(HostPlugStoreTopologyTarget, self).__init__()
    
        self.data['key'] = key
        self.data['transport'] = transport
    
    
    @property
    def key(self):
        '''The identifier of the target. This will be a string representing the transport
        information of the target.
        '''
        return self.data['key']

    @property
    def transport(self):
        '''Detailed, transport-specific information about the target of a path.
        '''
        return self.data['transport']

