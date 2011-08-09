
from pyvisdk.do.vm_config_spec import VmConfigSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VAppConfigSpec(VmConfigSpec):
    '''Configuration of a vApp
    '''
    
    def __init__(self, annotation, entityConfig, instanceUuid):
        # MUST define these
        super(VAppConfigSpec, self).__init__()
    
        self.data['annotation'] = annotation
        self.data['entityConfig'] = entityConfig
        self.data['instanceUuid'] = instanceUuid
    
    
    @property
    def annotation(self):
        '''Description for the vApp.
        '''
        return self.data['annotation']

    @property
    def entityConfig(self):
        '''Configuration of sub-entities (virtual machine or vApp container).
        '''
        return self.data['entityConfig']

    @property
    def instanceUuid(self):
        '''vCenter-specific 128-bit UUID of a vApp, represented as a hexadecimal string. This
        identifier is used by vCenter to uniquely identify all vApp instances in
        the Virtual Infrastructure environment.
        '''
        return self.data['instanceUuid']

