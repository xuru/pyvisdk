
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostAutoStartManagerConfig(DynamicData):
    '''Contains the entire auto-start/auto-stop configuration.
    '''
    
    def __init__(self, defaults, powerInfo):
        # MUST define these
        super(HostAutoStartManagerConfig, self).__init__()
    
        self.data['defaults'] = defaults
        self.data['powerInfo'] = powerInfo
    
    
    @property
    def defaults(self):
        '''System defaults for auto-start/auto-stop.
        '''
        return self.data['defaults']

    @property
    def powerInfo(self):
        '''Lists the auto-start/auto-stop configuration. If a virtual machine is not
        mentioned in this array, it does not participate in auto-start/auto-stop
        operations.
        '''
        return self.data['powerInfo']

