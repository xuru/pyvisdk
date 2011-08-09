
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostMultipathStateInfo(DynamicData):
    '''This data object type describes the state of storage paths on the host. All
        storage paths on the host are enumerated in this data object.The reason
        all path state information is encapsulated in this data object is because
        the path may actively change. This data object ensures that a request to
        gather path state changes only needs to fetch this data object.
    '''
    
    def __init__(self, path):
        # MUST define these
        super(HostMultipathStateInfo, self).__init__()
    
        self.data['path'] = path
    
    
    @property
    def path(self):
        '''List of paths on the system and their path states.
        '''
        return self.data['path']

