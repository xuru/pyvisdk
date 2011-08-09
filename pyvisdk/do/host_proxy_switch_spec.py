
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostProxySwitchSpec(DynamicData):
    '''This data object type describes the HostProxySwitch specification representing the
        properties on a HostProxySwitch that can be configured once the object
        exists.
    '''
    
    def __init__(self, backing):
        # MUST define these
        super(HostProxySwitchSpec, self).__init__()
    
        self.data['backing'] = backing
    
    
    @property
    def backing(self):
        '''The specification describes how physical network adapters are bridged to the
        switch.
        '''
        return self.data['backing']

