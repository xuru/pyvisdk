
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDiagnosticPartitionCreateSpec(DynamicData):
    '''The diagnostic create specification is used by the system to create a new
        diagnostic partition on a SCSI disk.
    '''
    
    def __init__(self, active, diagnosticType, id, partition, storageType):
        # MUST define these
        super(HostDiagnosticPartitionCreateSpec, self).__init__()
    
        self.data['active'] = active
        self.data['diagnosticType'] = diagnosticType
        self.data['id'] = id
        self.data['partition'] = partition
        self.data['storageType'] = storageType
    
    
    @property
    def active(self):
        '''Indicates if the created diagnostic partition should be made the active diagnostic
        partition. If not supplied, the system will decide whether or not the
        created specification is active.
        '''
        return self.data['active']

    @property
    def diagnosticType(self):
        '''Indicates the type of the diagnostic partition to be created.
        '''
        return self.data['diagnosticType']

    @property
    def id(self):
        '''Diagnostic partition identification information.
        '''
        return self.data['id']

    @property
    def partition(self):
        '''Partitioning specification.
        '''
        return self.data['partition']

    @property
    def storageType(self):
        '''Indicates the storage type where the diagnostic partition will be created.
        '''
        return self.data['storageType']

