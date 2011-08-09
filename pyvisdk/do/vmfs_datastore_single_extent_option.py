
from pyvisdk.do.vmfs_datastore_base_option import VmfsDatastoreBaseOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmfsDatastoreSingleExtentOption(VmfsDatastoreBaseOption):
    '''Datastore addition policy to use a single extent on the disk for a VMFS datastore.
        A single extent implies that one disk partition will be created on the
        disk for creating or increasing the capacity of a VMFS datastore.
    '''
    
    def __init__(self, vmfsExtent):
        # MUST define these
        super(VmfsDatastoreSingleExtentOption, self).__init__()
    
        self.data['vmfsExtent'] = vmfsExtent
    
    
    @property
    def vmfsExtent(self):
        '''The block range to be used as an extent in a VMFS datastore.
        '''
        return self.data['vmfsExtent']

