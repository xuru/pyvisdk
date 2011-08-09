
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmfsDatastoreSpec(DynamicData):
    '''Base class for VMFS datastore addition specification. Used as a generic way to
        point to one of the creation specifications that can be used to apply a
        specification to effect the creation or extension of a VMFS datastore.
    '''
    
    def __init__(self, diskUuid):
        # MUST define these
        super(VmfsDatastoreSpec, self).__init__()
    
        self.data['diskUuid'] = diskUuid
    
    
    @property
    def diskUuid(self):
        '''The UUID of the SCSI disk on which the VMFS datastore is located.
        '''
        return self.data['diskUuid']

