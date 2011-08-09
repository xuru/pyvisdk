
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDatastoreConnectInfo(DynamicData):
    '''The base data object type for information about datastores on the host.
    '''
    
    def __init__(self, summary):
        # MUST define these
        super(HostDatastoreConnectInfo, self).__init__()
    
        self.data['summary'] = summary
    
    
    @property
    def summary(self):
        '''Basic datastore information. The managed object reference is not set.
        '''
        return self.data['summary']

