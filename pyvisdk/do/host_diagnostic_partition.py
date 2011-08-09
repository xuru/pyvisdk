
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDiagnosticPartition(DynamicData):
    '''This data object type contains information about an available or active diagnostic
        partition.
    '''
    
    def __init__(self, diagnosticType, id, slots, storageType):
        # MUST define these
        super(HostDiagnosticPartition, self).__init__()
    
        self.data['diagnosticType'] = diagnosticType
        self.data['id'] = id
        self.data['slots'] = slots
        self.data['storageType'] = storageType
    
    
    @property
    def diagnosticType(self):
        '''Indicates the type of the diagnostic partition.
        '''
        return self.data['diagnosticType']

    @property
    def id(self):
        '''Diagnostic partition identification information.
        '''
        return self.data['id']

    @property
    def slots(self):
        '''The number of slots in the diagnostic partition.
        '''
        return self.data['slots']

    @property
    def storageType(self):
        '''Indicates the storage type of the diagnostic partition.
        '''
        return self.data['storageType']

