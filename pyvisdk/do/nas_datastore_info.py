
from pyvisdk.do.datastore_info import DatastoreInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NasDatastoreInfo(DatastoreInfo):
    '''Information details about a network-attached storage (NAS) datastore.
    '''
    
    def __init__(self, nas):
        # MUST define these
        super(NasDatastoreInfo, self).__init__()
    
        self.data['nas'] = nas
    
    
    @property
    def nas(self):
        '''The NFS mount information for the datastore. May not be available when the
        datastore is not accessible.
        '''
        return self.data['nas']

