
from pyvisdk.do.vmfs_datastore_spec import VmfsDatastoreSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmfsDatastoreCreateSpec(VmfsDatastoreSpec):
    '''This data object type is used when creating a new VMFS datastore, to create a
        specification for the VMFS datastore.
    '''
    
    def __init__(self, extent, partition, vmfs):
        # MUST define these
        super(VmfsDatastoreCreateSpec, self).__init__()
    
        self.data['extent'] = extent
        self.data['partition'] = partition
        self.data['vmfs'] = vmfs
    
    
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

    @property
    def vmfs(self):
        '''The VMFS creation specification.
        '''
        return self.data['vmfs']

