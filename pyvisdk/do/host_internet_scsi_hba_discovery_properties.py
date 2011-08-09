
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostInternetScsiHbaDiscoveryProperties(DynamicData):
    '''The discovery settings for this host bus adapter. At least one discovery mode must
        always be active. Multiple modes may be active at the same time.
    '''
    
    def __init__(self, iSnsDiscoveryEnabled, iSnsDiscoveryMethod, iSnsHost, sendTargetsDiscoveryEnabled, slpDiscoveryEnabled, slpDiscoveryMethod, slpHost, staticTargetDiscoveryEnabled):
        # MUST define these
        super(HostInternetScsiHbaDiscoveryProperties, self).__init__()
    
        self.data['iSnsDiscoveryEnabled'] = iSnsDiscoveryEnabled
        self.data['iSnsDiscoveryMethod'] = iSnsDiscoveryMethod
        self.data['iSnsHost'] = iSnsHost
        self.data['sendTargetsDiscoveryEnabled'] = sendTargetsDiscoveryEnabled
        self.data['slpDiscoveryEnabled'] = slpDiscoveryEnabled
        self.data['slpDiscoveryMethod'] = slpDiscoveryMethod
        self.data['slpHost'] = slpHost
        self.data['staticTargetDiscoveryEnabled'] = staticTargetDiscoveryEnabled
    
    
    @property
    def iSnsDiscoveryEnabled(self):
        '''True if iSNS is currently enabled
        '''
        return self.data['iSnsDiscoveryEnabled']

    @property
    def iSnsDiscoveryMethod(self):
        '''The iSNS discovery method in use when iSNS is enabled. Must be one of the values
        of InternetScsiSnsDiscoveryMethod
        '''
        return self.data['iSnsDiscoveryMethod']

    @property
    def iSnsHost(self):
        '''For STATIC iSNS, this is the iSNS server address
        '''
        return self.data['iSnsHost']

    @property
    def sendTargetsDiscoveryEnabled(self):
        '''True if send targets discovery is enabled
        '''
        return self.data['sendTargetsDiscoveryEnabled']

    @property
    def slpDiscoveryEnabled(self):
        '''True if SLP is enabled
        '''
        return self.data['slpDiscoveryEnabled']

    @property
    def slpDiscoveryMethod(self):
        '''The current SLP discovery method when SLP is enabled. Must be one of the values of
        SlpDiscoveryMethod
        '''
        return self.data['slpDiscoveryMethod']

    @property
    def slpHost(self):
        '''When the SLP discovery method is set to MANUAL, this property reflects the
        hostname, and optionally port number of the SLP DA.
        '''
        return self.data['slpHost']

    @property
    def staticTargetDiscoveryEnabled(self):
        '''True if static target discovery is enabled
        '''
        return self.data['staticTargetDiscoveryEnabled']

