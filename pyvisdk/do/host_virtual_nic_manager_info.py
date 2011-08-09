
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVirtualNicManagerInfo(DynamicData):
    '''This data object type describes VirtualNic host configuration data objects.
    '''
    
    def __init__(self, netConfig):
        # MUST define these
        super(HostVirtualNicManagerInfo, self).__init__()
    
        self.data['netConfig'] = netConfig
    
    
    @property
    def netConfig(self):
        '''List of VirtualNicManager network configuration.
        '''
        return self.data['netConfig']

