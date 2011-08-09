
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ImportSpec(DynamicData):
    '''An ImportSpec is used when importing VMs or vApps.It can be built from scratch, or
        it can be generated from an OVF descriptor using the service interface
        OvfManager.This class is the abstract base for VirtualMachineImportSpec
        and VirtualAppImportSpec. These three classes form a composite structure
        that allows us to contain arbitrarily complex entitites in a single
        ImportSpec.
    '''
    
    def __init__(self, entityConfig):
        # MUST define these
        super(ImportSpec, self).__init__()
    
        self.data['entityConfig'] = entityConfig
    
    
    @property
    def entityConfig(self):
        '''Configuration of sub-entities (virtual machine or vApp). This is used for sub-
        entities of a vApp that could be a virtual machine or a vApp.
        '''
        return self.data['entityConfig']

