
from pyvisdk.do.host_hardware_element_info import HostHardwareElementInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostStorageElementInfo(HostHardwareElementInfo):
    '''Data object describing the operational status of various storage elements.
    '''
    
    def __init__(self, operationalInfo):
        # MUST define these
        super(HostStorageElementInfo, self).__init__()
    
        self.data['operationalInfo'] = operationalInfo
    
    
    @property
    def operationalInfo(self):
        '''Other information regarding the operational state of the storage element.
        '''
        return self.data['operationalInfo']

