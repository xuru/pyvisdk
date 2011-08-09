
from pyvisdk.do.dvs_event import DvsEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DvsUpgradeAvailableEvent(DvsEvent):
    '''An upgrade for the distributed virtual switch is available.
    '''
    
    def __init__(self, productInfo):
        # MUST define these
        super(DvsUpgradeAvailableEvent, self).__init__()
    
        self.data['productInfo'] = productInfo
    
    
    @property
    def productInfo(self):
        '''The product info of the upgrade.
        '''
        return self.data['productInfo']

