
from pyvisdk.do.vmfs_datastore_single_extent_option import VmfsDatastoreSingleExtentOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmfsDatastoreAllExtentOption(VmfsDatastoreSingleExtentOption):
    '''Datastore addition policy to use the entire disk as a single extent for a VMFS
        datastore. If there is any data on the disk, it will be overwritten.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(VmfsDatastoreAllExtentOption, self).__init__()
    

    
    
