
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DatastoreHostMount(DynamicData):
    '''Host-specific datastore information.
    '''
    
    def __init__(self, key, mountInfo):
        # MUST define these
        super(DatastoreHostMount, self).__init__()
    
        self.data['key'] = key
        self.data['mountInfo'] = mountInfo
    
    
    @property
    def key(self):
        '''The host associated with this datastore.
        '''
        return self.data['key']

    @property
    def mountInfo(self):
        '''Host-specific information about the mount.
        '''
        return self.data['mountInfo']

