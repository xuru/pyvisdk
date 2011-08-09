
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HttpNfcLeaseDatastoreLeaseInfo(DynamicData):
    '''For a given datastore, represented by datastoreKey, contains a list of leased
        multi-POST-capable hosts connected to it.
    '''
    
    def __init__(self, datastoreKey, hosts):
        # MUST define these
        super(HttpNfcLeaseDatastoreLeaseInfo, self).__init__()
    
        self.data['datastoreKey'] = datastoreKey
        self.data['hosts'] = hosts
    
    
    @property
    def datastoreKey(self):
        '''Datastore key.
        '''
        return self.data['datastoreKey']

    @property
    def hosts(self):
        '''List of hosts connected to this datastore and covered by this lease. The hosts in
        this list are multi-POST-capable, and any one of them can be used to
        transfer disks on this datastore.
        '''
        return self.data['hosts']

