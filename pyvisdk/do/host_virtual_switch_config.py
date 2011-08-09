
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVirtualSwitchConfig(DynamicData):
    '''This data object type describes the VirtualSwitch configuration containing both
        the configurable properties on a VirtualSwitch and identification
        information.
    '''
    
    def __init__(self, changeOperation, name, spec):
        # MUST define these
        super(HostVirtualSwitchConfig, self).__init__()
    
        self.data['changeOperation'] = changeOperation
        self.data['name'] = name
        self.data['spec'] = spec
    
    
    @property
    def changeOperation(self):
        '''This property indicates the change operation to apply on this configuration
        specification.
        '''
        return self.data['changeOperation']

    @property
    def name(self):
        '''The name of the virtual switch. Maximum length is 32 characters.
        '''
        return self.data['name']

    @property
    def spec(self):
        '''The specification of the VirtualSwitch.
        '''
        return self.data['spec']

