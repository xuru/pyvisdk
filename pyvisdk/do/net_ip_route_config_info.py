
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NetIpRouteConfigInfo(DynamicData):
    '''This data object reports the IP Route Table.
    '''
    
    def __init__(self, ipRoute):
        # MUST define these
        super(NetIpRouteConfigInfo, self).__init__()
    
        self.data['ipRoute'] = ipRoute
    
    
    @property
    def ipRoute(self):
        '''IP routing table for all address families.
        '''
        return self.data['ipRoute']

