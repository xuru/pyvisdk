
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDiagnosticPartitionCreateOption(DynamicData):
    '''This data object describes a disk that can be used to create a diagnostic
        partition.
    '''
    
    def __init__(self, diagnosticType, disk, storageType):
        # MUST define these
        super(HostDiagnosticPartitionCreateOption, self).__init__()
    
        self.data['diagnosticType'] = diagnosticType
        self.data['disk'] = disk
        self.data['storageType'] = storageType
    
    
    @property
    def diagnosticType(self):
        '''Indicates the type of the diagnostic partition to be created.
        '''
        return self.data['diagnosticType']

    @property
    def disk(self):
        '''The disk which has sufficient free space to contain a diagnostic partition.
        '''
        return self.data['disk']

    @property
    def storageType(self):
        '''Indicates the storage type of diagnostic partition to be created.
        '''
        return self.data['storageType']

