
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostInternetScsiHbaDiscoveryCapabilities(DynamicData):
    '''The discovery capabilities for this host bus adapter. At least one discovery mode
        must always be active. Multiple modes may be active at the same time.
    '''
    
    def __init__(self, iSnsDiscoverySettable, sendTargetsDiscoverySettable, slpDiscoverySettable, staticTargetDiscoverySettable):
        # MUST define these
        super(HostInternetScsiHbaDiscoveryCapabilities, self).__init__()
    
        self.data['iSnsDiscoverySettable'] = iSnsDiscoverySettable
        self.data['sendTargetsDiscoverySettable'] = sendTargetsDiscoverySettable
        self.data['slpDiscoverySettable'] = slpDiscoverySettable
        self.data['staticTargetDiscoverySettable'] = staticTargetDiscoverySettable
    
    
    @property
    def iSnsDiscoverySettable(self):
        '''True if this host bus adapter supports iSNS
        '''
        return self.data['iSnsDiscoverySettable']

    @property
    def sendTargetsDiscoverySettable(self):
        '''True if this host bus adapter supports changing the configuration state of send
        targets discovery. Send targets is mandatory, however some adapters may
        not allow disabling this discovery method.
        '''
        return self.data['sendTargetsDiscoverySettable']

    @property
    def slpDiscoverySettable(self):
        '''True if this host bus adapter supports SLP
        '''
        return self.data['slpDiscoverySettable']

    @property
    def staticTargetDiscoverySettable(self):
        '''True if this host bus adapter supports static discovery
        '''
        return self.data['staticTargetDiscoverySettable']

