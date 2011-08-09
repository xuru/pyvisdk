
from pyvisdk.do.template_upgrade_event import TemplateUpgradeEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class TemplateUpgradeFailedEvent(TemplateUpgradeEvent):
    '''This event records that the template upgrade failed.
    '''
    
    def __init__(self, reason):
        # MUST define these
        super(TemplateUpgradeFailedEvent, self).__init__()
    
        self.data['reason'] = reason
    
    
    @property
    def reason(self):
        '''
        '''
        return self.data['reason']

