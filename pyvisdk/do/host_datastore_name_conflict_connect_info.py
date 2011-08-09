
from pyvisdk.do.host_datastore_connect_info import HostDatastoreConnectInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDatastoreNameConflictConnectInfo(HostDatastoreConnectInfo):
    '''This data object type describes a datastore on the host that has the same name as
        a different datastore on VirtualCenter.
    '''
    
    def __init__(self, newDatastoreName):
        # MUST define these
        super(HostDatastoreNameConflictConnectInfo, self).__init__()
    
        self.data['newDatastoreName'] = newDatastoreName
    
    
    @property
    def newDatastoreName(self):
        '''To resolve a conflict with existing datastores, a suggested new name of the
        datastore can be provided.
        '''
        return self.data['newDatastoreName']

