
from pyvisdk.do.host_datastore_connect_info import HostDatastoreConnectInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDatastoreExistsConnectInfo(HostDatastoreConnectInfo):
    '''This data object type describes a datastore on the host that matches an existing
        datastore on VirtualCenter that has a different name.
    '''
    
    def __init__(self, newDatastoreName):
        # MUST define these
        super(HostDatastoreExistsConnectInfo, self).__init__()
    
        self.data['newDatastoreName'] = newDatastoreName
    
    
    @property
    def newDatastoreName(self):
        '''The name of a matching datastore on VirtualCenter. The datastore on the host will
        be renamed to this name.
        '''
        return self.data['newDatastoreName']

