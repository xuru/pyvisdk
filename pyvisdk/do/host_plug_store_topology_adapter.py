
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPlugStoreTopologyAdapter(DynamicData):
    '''This data object type is an association class that describes a host bus adapter
        and its associated storage Paths. The set of Paths on all the host bus
        adapters is the complete set of Paths in the system.
    '''
    
    def __init__(self, adapter, key, path):
        # MUST define these
        super(HostPlugStoreTopologyAdapter, self).__init__()
    
        self.data['adapter'] = adapter
        self.data['key'] = key
        self.data['path'] = path
    
    
    @property
    def adapter(self):
        '''The link to the host bus adapter for this inebtrface.
        '''
        return self.data['adapter']

    @property
    def key(self):
        '''The identifier for the host bus adapter.
        '''
        return self.data['key']

    @property
    def path(self):
        '''The list of paths to which the host bus adapter is associated.
        '''
        return self.data['path']

