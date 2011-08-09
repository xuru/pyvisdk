
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitchKeyedOpaqueBlob(DynamicData):
    '''This class defines a data structure to hold opaque binary data identified by a
        key.
    '''
    
    def __init__(self, key, opaqueData):
        # MUST define these
        super(DistributedVirtualSwitchKeyedOpaqueBlob, self).__init__()
    
        self.data['key'] = key
        self.data['opaqueData'] = opaqueData
    
    
    @property
    def key(self):
        '''A key that identifies the opaque binary blob.
        '''
        return self.data['key']

    @property
    def opaqueData(self):
        '''The opaque data. It is recommended that base64 encoding be used for binary data.
        '''
        return self.data['opaqueData']

