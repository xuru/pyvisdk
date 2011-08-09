
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NetIpRouteConfigSpec(DynamicData):
    '''Address family independent IP Route Table Configuration data object.
    '''
    
    def __init__(self, ipRoute):
        # MUST define these
        super(NetIpRouteConfigSpec, self).__init__()
    
        self.data['ipRoute'] = ipRoute
    
    
    @property
    def ipRoute(self):
        '''The set of updates to apply to the routing table.
        '''
        return self.data['ipRoute']

