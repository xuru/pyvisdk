
from pyvisdk.do.event import Event
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class UpgradeEvent(Event):
    '''These event types represent events converted from VirtualCenter 1.x. All upgraded
        events are converted to string values.
    '''
    
    def __init__(self, message):
        # MUST define these
        super(UpgradeEvent, self).__init__()
    
        self.data['message'] = message
    
    
    @property
    def message(self):
        '''The formatted message from the upgrade.
        '''
        return self.data['message']

