
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostProxySwitchConfig(DynamicData):
    '''This data object type describes the HostProxySwitch configuration containing both
        the configurable properties on a HostProxySwitch and identification
        information.
    '''
    
    def __init__(self, changeOperation, spec, uuid):
        # MUST define these
        super(HostProxySwitchConfig, self).__init__()
    
        self.data['changeOperation'] = changeOperation
        self.data['spec'] = spec
        self.data['uuid'] = uuid
    
    
    @property
    def changeOperation(self):
        '''This property indicates the change operation to apply on this configuration
        specification. Valid values are: * edit * remove
        '''
        return self.data['changeOperation']

    @property
    def spec(self):
        '''The specification of the HostProxySwitch.
        '''
        return self.data['spec']

    @property
    def uuid(self):
        '''The uuid of the DistributedVirtualSwitch that the HostProxySwitch is a part of.
        '''
        return self.data['uuid']

