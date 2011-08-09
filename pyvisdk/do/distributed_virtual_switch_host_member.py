
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitchHostMember(DynamicData):
    '''The data object that represents a host member in the distributed virtual switch.
    '''
    
    def __init__(self, config, productInfo, status, statusDetail, uplinkPortKey):
        # MUST define these
        super(DistributedVirtualSwitchHostMember, self).__init__()
    
        self.data['config'] = config
        self.data['productInfo'] = productInfo
        self.data['status'] = status
        self.data['statusDetail'] = statusDetail
        self.data['uplinkPortKey'] = uplinkPortKey
    
    
    @property
    def config(self):
        '''Host member configuration.
        '''
        return self.data['config']

    @property
    def productInfo(self):
        '''The vendor, product and version information for the proxy vSwitch module.
        '''
        return self.data['productInfo']

    @property
    def status(self):
        '''The host DistributedVirtualSwitch component status. See HostComponentState for
        valid values.
        '''
        return self.data['status']

    @property
    def statusDetail(self):
        '''Additional information regarding the host's current status.
        '''
        return self.data['statusDetail']

    @property
    def uplinkPortKey(self):
        '''The port keys of the uplink ports created for the host member. These ports will be
        deleted after the host leaves the switch.
        '''
        return self.data['uplinkPortKey']

