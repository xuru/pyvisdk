
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVSCapability(DynamicData):
    '''Capability of the switch configuration.
    '''
    
    def __init__(self, compatibleHostComponentProductInfo, dvPortGroupOperationSupported, dvPortOperationSupported, dvsOperationSupported, featuresSupported):
        # MUST define these
        super(DVSCapability, self).__init__()
    
        self.data['compatibleHostComponentProductInfo'] = compatibleHostComponentProductInfo
        self.data['dvPortGroupOperationSupported'] = dvPortGroupOperationSupported
        self.data['dvPortOperationSupported'] = dvPortOperationSupported
        self.data['dvsOperationSupported'] = dvsOperationSupported
        self.data['featuresSupported'] = featuresSupported
    
    
    @property
    def compatibleHostComponentProductInfo(self):
        '''The list of host component product information that is compatible with the current
        switch implementation.
        '''
        return self.data['compatibleHostComponentProductInfo']

    @property
    def dvPortGroupOperationSupported(self):
        '''Whether this switch allows vCenter users to modify DVS configuration at the
        portgroup level, except for host member, policy, and scope operations.
        '''
        return self.data['dvPortGroupOperationSupported']

    @property
    def dvPortOperationSupported(self):
        '''Whether this switch allows vCenter users to modify DVS configuration at the port
        level, except for host member, policy, and scope operations.
        '''
        return self.data['dvPortOperationSupported']

    @property
    def dvsOperationSupported(self):
        '''Whether this switch allows vCenter users to modify DVS configuration at the switch
        level, except for host member, policy, and scope operations.
        '''
        return self.data['dvsOperationSupported']

    @property
    def featuresSupported(self):
        '''Indicators for which version-specific DVS features are available on this switch.
        This information is read-only; it cannot be specified when creating a DVS,
        and it cannot be modified by UpdateDvsCapability.
        '''
        return self.data['featuresSupported']

