
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineTargetInfo(DynamicData):
    '''The TargetInfo specified a value that can be used in the device backings to
        connect the virtual machine to a physical (or logical) host device.
    '''
    
    def __init__(self, configurationTag, name):
        # MUST define these
        super(VirtualMachineTargetInfo, self).__init__()
    
        self.data['configurationTag'] = configurationTag
        self.data['name'] = name
    
    
    @property
    def configurationTag(self):
        '''List of configurations that this device is available for. This is only filled out
        if more than one configuration is requested.
        '''
        return self.data['configurationTag']

    @property
    def name(self):
        '''The identification of the endpoint on the host. The format of this depends on the
        kind of virtual device this endpoints is used for. For example, for a
        VirtualEthernetCard this would be a networkname, and for a VirtualCDROM it
        would be a device name.
        '''
        return self.data['name']

