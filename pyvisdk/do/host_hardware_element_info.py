
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostHardwareElementInfo(DynamicData):
    '''Data object describing the operational status of a physical element.
    '''
    
    def __init__(self, name, status):
        # MUST define these
        super(HostHardwareElementInfo, self).__init__()
    
        self.data['name'] = name
        self.data['status'] = status
    
    
    @property
    def name(self):
        '''The name of the physical element
        '''
        return self.data['name']

    @property
    def status(self):
        '''The operational status of the physical element. The status is one of the values
        specified in HostHardwareElementStatus.
        '''
        return self.data['status']

