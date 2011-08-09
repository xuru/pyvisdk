
from pyvisdk.do.dvs_event import DvsEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DvsUpgradeRejectedEvent(DvsEvent):
    '''An upgrade for the distributed virtual switch is rejected.
    '''
    
    def __init__(self, productInfo):
        # MUST define these
        super(DvsUpgradeRejectedEvent, self).__init__()
    
        self.data['productInfo'] = productInfo
    
    
    @property
    def productInfo(self):
        '''The product info of the upgrade.
        '''
        return self.data['productInfo']

