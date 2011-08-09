
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PhysicalNicLinkInfo(DynamicData):
    '''This data object type describes the link speed and the type of duplex
        communication. The link speed indicates the bit rate in Mhz. The duplex
        boolean indicates if the link is capable of full-duplex or half-duplex
        communication.
    '''
    
    def __init__(self, duplex, speedMb):
        # MUST define these
        super(PhysicalNicLinkInfo, self).__init__()
    
        self.data['duplex'] = duplex
        self.data['speedMb'] = speedMb
    
    
    @property
    def duplex(self):
        '''The flag to indicate whether or not the link is capable of full-duplex ("true") or
        only half-duplex ("false").
        '''
        return self.data['duplex']

    @property
    def speedMb(self):
        '''The bit rate on the link.
        '''
        return self.data['speedMb']

