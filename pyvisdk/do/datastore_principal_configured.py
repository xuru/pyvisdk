
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DatastorePrincipalConfigured(HostEvent):
    '''This event records that a datastore principal was configured on a host.
    '''
    
    def __init__(self, datastorePrincipal):
        # MUST define these
        super(DatastorePrincipalConfigured, self).__init__()
    
        self.data['datastorePrincipal'] = datastorePrincipal
    
    
    @property
    def datastorePrincipal(self):
        '''
        '''
        return self.data['datastorePrincipal']

