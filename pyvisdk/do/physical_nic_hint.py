
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PhysicalNicHint(DynamicData):
    '''This data object type describes each network of a physical network adapter's
        network hint.
    '''
    
    def __init__(self, vlanId):
        # MUST define these
        super(PhysicalNicHint, self).__init__()
    
        self.data['vlanId'] = vlanId
    
    
    @property
    def vlanId(self):
        '''The optional VLAN Id of the network.
        '''
        return self.data['vlanId']

