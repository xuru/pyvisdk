
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VMwareDVSPvlanConfigSpec(DynamicData):
    '''This class defines the configuration of a PVLAN map entry
    '''
    
    def __init__(self, operation, pvlanEntry):
        # MUST define these
        super(VMwareDVSPvlanConfigSpec, self).__init__()
    
        self.data['operation'] = operation
        self.data['pvlanEntry'] = pvlanEntry
    
    
    @property
    def operation(self):
        '''Operation type. See ConfigSpecOperation for valid values, except for the "edit"
        value, which is not supported.
        '''
        return self.data['operation']

    @property
    def pvlanEntry(self):
        '''The PVLAN entry to be added or removed.
        '''
        return self.data['pvlanEntry']

