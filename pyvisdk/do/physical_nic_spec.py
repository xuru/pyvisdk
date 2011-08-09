
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PhysicalNicSpec(DynamicData):
    '''This data object type describes the physical network adapter specification
        representing the properties on a physical network adapter that can be
        configured once the object exists.
    '''
    
    def __init__(self, ip, linkSpeed):
        # MUST define these
        super(PhysicalNicSpec, self).__init__()
    
        self.data['ip'] = ip
        self.data['linkSpeed'] = linkSpeed
    
    
    @property
    def ip(self):
        '''The IP configuration on the physical network adapter (applies only to a hosted
        network adapter). The data object will be NULL on an ESX Server system.
        '''
        return self.data['ip']

    @property
    def linkSpeed(self):
        '''The link speed and duplexity that this physical network adapter is currently
        configured to use. If this property is not set, the physical network
        adapter autonegotiates its proper settings.
        '''
        return self.data['linkSpeed']

