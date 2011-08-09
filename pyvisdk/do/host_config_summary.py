
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostConfigSummary(DynamicData):
    '''An overview of the key configuration parameters.
    '''
    
    def __init__(self, faultToleranceEnabled, featureVersion, name, port, product, sslThumbprint, vmotionEnabled):
        # MUST define these
        super(HostConfigSummary, self).__init__()
    
        self.data['faultToleranceEnabled'] = faultToleranceEnabled
        self.data['featureVersion'] = featureVersion
        self.data['name'] = name
        self.data['port'] = port
        self.data['product'] = product
        self.data['sslThumbprint'] = sslThumbprint
        self.data['vmotionEnabled'] = vmotionEnabled
    
    
    @property
    def faultToleranceEnabled(self):
        '''The flag to indicate whether or not Fault Tolerance logging is enabled on this
        host.
        '''
        return self.data['faultToleranceEnabled']

    @property
    def featureVersion(self):
        '''List of feature-specific version information. Each element refers to the version
        information for a specific feature.
        '''
        return self.data['featureVersion']

    @property
    def name(self):
        '''The name of the host.
        '''
        return self.data['name']

    @property
    def port(self):
        '''The port number.
        '''
        return self.data['port']

    @property
    def product(self):
        '''Information about the software running on the host, if known.
        '''
        return self.data['product']

    @property
    def sslThumbprint(self):
        '''The SSL thumbprint of the host, if known.
        '''
        return self.data['sslThumbprint']

    @property
    def vmotionEnabled(self):
        '''The flag to indicate whether or not VMotion is enabled on this host.
        '''
        return self.data['vmotionEnabled']

