
from pyvisdk.do.datastore_info import DatastoreInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmfsDatastoreInfo(DatastoreInfo):
    '''Information details about a VMFS datastore.
    '''
    
    def __init__(self, vmfs):
        # MUST define these
        super(VmfsDatastoreInfo, self).__init__()
    
        self.data['vmfs'] = vmfs
    
    
    @property
    def vmfs(self):
        '''The VMFS volume information for the datastore. May not be available when the
        datastore is not accessible.
        '''
        return self.data['vmfs']

