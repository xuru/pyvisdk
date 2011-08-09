
from pyvisdk.do.event import Event
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class TemplateUpgradeEvent(Event):
    '''This event is the base class for all the template upgrade events.
    '''
    
    def __init__(self, legacyTemplate):
        # MUST define these
        super(TemplateUpgradeEvent, self).__init__()
    
        self.data['legacyTemplate'] = legacyTemplate
    
    
    @property
    def legacyTemplate(self):
        '''
        '''
        return self.data['legacyTemplate']

