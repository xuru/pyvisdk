
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NetIpRouteConfigInfoGateway(DynamicData):
    '''Next hop Gateway for a given route.
    '''
    
    def __init__(self, device, ipAddress):
        # MUST define these
        super(NetIpRouteConfigInfoGateway, self).__init__()
    
        self.data['device'] = device
        self.data['ipAddress'] = ipAddress
    
    
    @property
    def device(self):
        '''
        '''
        return self.data['device']

    @property
    def ipAddress(self):
        '''
        '''
        return self.data['ipAddress']

