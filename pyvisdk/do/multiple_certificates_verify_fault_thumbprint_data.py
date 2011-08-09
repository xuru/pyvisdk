
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class MultipleCertificatesVerifyFaultThumbprintData(DynamicData):
    '''
    '''
    
    def __init__(self, port, thumbprint):
        # MUST define these
        super(MultipleCertificatesVerifyFaultThumbprintData, self).__init__()
    
        self.data['port'] = port
        self.data['thumbprint'] = thumbprint
    
    
    @property
    def port(self):
        '''The port used by the service.
        '''
        return self.data['port']

    @property
    def thumbprint(self):
        '''The SSL thumbprint of the host's certificate used by the service.
        '''
        return self.data['thumbprint']

