
from pyvisdk.do.vmfs_datastore_base_option import VmfsDatastoreBaseOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmfsDatastoreMultipleExtentOption(VmfsDatastoreBaseOption):
    '''Datastore addition policy to use multiple extents on the disk for a VMFS
        datastore. Multiple extents implies that more than one disk partition will
        be created on the disk for creating or increasing the capacity of a VMFS
        datastore. Multiple extents are needed when unpartitioned space is
        fragmented in the existing partition layout of the disk.
    '''
    
    def __init__(self, vmfsExtent):
        # MUST define these
        super(VmfsDatastoreMultipleExtentOption, self).__init__()
    
        self.data['vmfsExtent'] = vmfsExtent
    
    
    @property
    def vmfsExtent(self):
        '''The block ranges to be used as extents in a VMFS datastore. The first block range
        will be the head partition.
        '''
        return self.data['vmfsExtent']

