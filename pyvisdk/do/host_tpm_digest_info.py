
from pyvisdk.do.host_digest_info import HostDigestInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostTpmDigestInfo(HostDigestInfo):
    '''This data object type describes the digest values in the Platform Configuration
        Register (PCR) of a Trusted Platform Module (TPM) device.
    '''
    
    def __init__(self, pcrNumber):
        # MUST define these
        super(HostTpmDigestInfo, self).__init__()
    
        self.data['pcrNumber'] = pcrNumber
    
    
    @property
    def pcrNumber(self):
        '''Index of the PCR that stores the TPM digest value.
        '''
        return self.data['pcrNumber']

