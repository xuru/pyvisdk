
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NetIpStackInfo(DynamicData):
    '''Protocol version independent reporting data object for IP stack.
    '''
    
    def __init__(self, defaultRouter, neighbor):
        # MUST define these
        super(NetIpStackInfo, self).__init__()
    
        self.data['defaultRouter'] = defaultRouter
        self.data['neighbor'] = neighbor
    
    
    @property
    def defaultRouter(self):
        '''Zero one or more entries of discovered IP routers that are directly reachable from
        a an interface on this system. This property maps to RFC 4293
        ipDefaultRouterTable.
        '''
        return self.data['defaultRouter']

    @property
    def neighbor(self):
        '''Zero, one or more entries of neighbors discovered using ARP or NDP. This
        information is used to help diagnose connectivity or performance issues.
        This property maps to RFC 4293 ipNetToPhysicalTable.
        '''
        return self.data['neighbor']

