
from pyvisdk.do.dvs_event import DvsEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DvsUpgradedEvent(DvsEvent):
    '''The distributed virtual switch was upgraded.
    '''
    
    def __init__(self, productInfo):
        # MUST define these
        super(DvsUpgradedEvent, self).__init__()
    
        self.data['productInfo'] = productInfo
    
    
    @property
    def productInfo(self):
        '''The product info of the upgrade.
        '''
        return self.data['productInfo']

