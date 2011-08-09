
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitchHostMemberPnicSpec(DynamicData):
    '''Specification to select individual physical NICs. In this case, a proxy switch
        will be created on the host from scratch with the pNICs as the uplinks.
    '''
    
    def __init__(self, connectionCookie, pnicDevice, uplinkPortgroupKey, uplinkPortKey):
        # MUST define these
        super(DistributedVirtualSwitchHostMemberPnicSpec, self).__init__()
    
        self.data['connectionCookie'] = connectionCookie
        self.data['pnicDevice'] = pnicDevice
        self.data['uplinkPortgroupKey'] = uplinkPortgroupKey
        self.data['uplinkPortKey'] = uplinkPortKey
    
    
    @property
    def connectionCookie(self):
        '''The cookie that represents this portConnection instance for the port. The value of
        this property is generated from the Server. Any value set by an SDK client
        is ignored.
        '''
        return self.data['connectionCookie']

    @property
    def pnicDevice(self):
        '''The physical NIC to be added in the switch. See device.
        '''
        return self.data['pnicDevice']

    @property
    def uplinkPortgroupKey(self):
        '''The key of the portgroup to be connected to the physical NIC.
        '''
        return self.data['uplinkPortgroupKey']

    @property
    def uplinkPortKey(self):
        '''The key of the port to be connected to the physical NICs.
        '''
        return self.data['uplinkPortKey']

