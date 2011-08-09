
from pyvisdk.do.entity_event_argument import EntityEventArgument
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ScheduledTaskEventArgument(EntityEventArgument):
    '''The event argument is a scheduled task object.
    '''
    
    def __init__(self, scheduledTask):
        # MUST define these
        super(ScheduledTaskEventArgument, self).__init__()
    
        self.data['scheduledTask'] = scheduledTask
    
    
    @property
    def scheduledTask(self):
        '''The scheduled task object.
        '''
        return self.data['scheduledTask']

