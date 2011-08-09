
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostIpRouteOp(DynamicData):
    '''Routing Entry Operation. Routing entries are individual static routes which
        combined with the default route form all of the routing rules for a host.
    '''
    
    def __init__(self, changeOperation, route):
        # MUST define these
        super(HostIpRouteOp, self).__init__()
    
        self.data['changeOperation'] = changeOperation
        self.data['route'] = route
    
    
    @property
    def changeOperation(self):
        '''This property indicates the change operation to apply on this configuration
        specification.
        '''
        return self.data['changeOperation']

    @property
    def route(self):
        '''The routing entry itself
        '''
        return self.data['route']

