
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterDasAamNodeState(DynamicData):
    '''The ClusterDasAamNodeState data object represents the state of the HA service on
        an ESX host. (AAM is a component of this service.)
    '''
    
    def __init__(self, configState, host, name, runtimeState):
        # MUST define these
        super(ClusterDasAamNodeState, self).__init__()
    
        self.data['configState'] = configState
        self.data['host'] = host
        self.data['name'] = name
        self.data['runtimeState'] = runtimeState
    
    
    @property
    def configState(self):
        '''Configuration state of the HA agent on the host. The property can be one of the
        following values:
        '''
        return self.data['configState']

    @property
    def host(self):
        '''Reference to the host.
        '''
        return self.data['host']

    @property
    def name(self):
        '''Name of the host (HostSystem.name).
        '''
        return self.data['name']

    @property
    def runtimeState(self):
        '''The runtime state of the HA agent on the node. The property can be one of the
        following values:
        '''
        return self.data['runtimeState']

