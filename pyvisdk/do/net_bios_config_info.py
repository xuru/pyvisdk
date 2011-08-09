
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NetBIOSConfigInfo(DynamicData):
    '''This data object type describes the NetBIOS configuration of an operating system.
    '''
    
    def __init__(self, mode):
        # MUST define these
        super(NetBIOSConfigInfo, self).__init__()
    
        self.data['mode'] = mode
    
    
    @property
    def mode(self):
        '''NetBIOS configuration mode. The supported values are described by
        NetBIOSConfigInfoMode.
        '''
        return self.data['mode']

