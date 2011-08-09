
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVMotionConfig(DynamicData):
    '''This data object configuring VMotion on the host. The runtime information is
        available from the VMotionInfo data object type.
    '''
    
    def __init__(self, enabled, vmotionNicKey):
        # MUST define these
        super(HostVMotionConfig, self).__init__()
    
        self.data['enabled'] = enabled
        self.data['vmotionNicKey'] = vmotionNicKey
    
    
    @property
    def enabled(self):
        '''Flag to indicate whether or not VMotion is enabled.
        '''
        return self.data['enabled']

    @property
    def vmotionNicKey(self):
        '''Key of the VirtualNic used for VMotion.
        '''
        return self.data['vmotionNicKey']

