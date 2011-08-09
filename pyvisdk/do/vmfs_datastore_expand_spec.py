
from pyvisdk.do.vmfs_datastore_spec import VmfsDatastoreSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmfsDatastoreExpandSpec(VmfsDatastoreSpec):
    '''Specification to increase the capacity of a VMFS datastore by expanding
        (increasing the size of) an existing extent of the datastore.
    '''
    
    def __init__(self, extent, partition):
        # MUST define these
        super(VmfsDatastoreExpandSpec, self).__init__()
    
        self.data['extent'] = extent
        self.data['partition'] = partition
    
    
    @property
    def extent(self):
        '''VMFS extent to expand.
        '''
        return self.data['extent']

    @property
    def partition(self):
        '''Partitioning specification.
        '''
        return self.data['partition']

