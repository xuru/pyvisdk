
from pyvisdk.do.vmfs_datastore_spec import VmfsDatastoreSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmfsDatastoreExtendSpec(VmfsDatastoreSpec):
    '''Specification to increase the capacity of a VMFS datastore by adding one or more
        new extents to the datastore. All the extents to be added must be on the
        same disk. Extension is different from creation in that the VMFS creation
        specification need not be specified.
    '''
    
    def __init__(self, extent, partition):
        # MUST define these
        super(VmfsDatastoreExtendSpec, self).__init__()
    
        self.data['extent'] = extent
        self.data['partition'] = partition
    
    
    @property
    def extent(self):
        '''Extents to append to VMFS.
        '''
        return self.data['extent']

    @property
    def partition(self):
        '''Partitioning specification.
        '''
        return self.data['partition']

