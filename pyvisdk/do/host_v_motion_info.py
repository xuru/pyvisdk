
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVMotionInfo(DynamicData):
    '''This data object type describes VMotion host configuration data objects.
    '''
    
    def __init__(self, ipConfig, netConfig):
        # MUST define these
        super(HostVMotionInfo, self).__init__()
    
        self.data['ipConfig'] = ipConfig
        self.data['netConfig'] = netConfig
    
    
    @property
    def ipConfig(self):
        '''IP configuration of the VMotion VirtualNic.
        '''
        return self.data['ipConfig']

    @property
    def netConfig(self):
        '''VMotion network configuration.
        '''
        return self.data['netConfig']

