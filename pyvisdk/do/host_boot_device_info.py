
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostBootDeviceInfo(DynamicData):
    '''This data object represents the boot device information of the host.
    '''
    
    def __init__(self, bootDevices, currentBootDeviceKey):
        # MUST define these
        super(HostBootDeviceInfo, self).__init__()
    
        self.data['bootDevices'] = bootDevices
        self.data['currentBootDeviceKey'] = currentBootDeviceKey
    
    
    @property
    def bootDevices(self):
        '''The list of boot devices present on the host
        '''
        return self.data['bootDevices']

    @property
    def currentBootDeviceKey(self):
        '''The key of the current boot device that the host is configured to boot. This
        property is unset if the current boot device is disabled.
        '''
        return self.data['currentBootDeviceKey']

