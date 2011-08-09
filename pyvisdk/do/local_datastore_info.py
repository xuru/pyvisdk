
from pyvisdk.do.datastore_info import DatastoreInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LocalDatastoreInfo(DatastoreInfo):
    '''The information details about a datastore that is local to a host.
    '''
    
    def __init__(self, path):
        # MUST define these
        super(LocalDatastoreInfo, self).__init__()
    
        self.data['path'] = path
    
    
    @property
    def path(self):
        '''The local path on a host. May not be available when the datastore is not
        accessible.
        '''
        return self.data['path']

