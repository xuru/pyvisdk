
from pyvisdk.do.event import Event
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ScheduledTaskEvent(Event):
    '''These events are scheduled task events.
    '''
    
    def __init__(self, entity, scheduledTask):
        # MUST define these
        super(ScheduledTaskEvent, self).__init__()
    
        self.data['entity'] = entity
        self.data['scheduledTask'] = scheduledTask
    
    
    @property
    def entity(self):
        '''The entity on which the scheduled task registered.
        '''
        return self.data['entity']

    @property
    def scheduledTask(self):
        '''The scheduled task object.
        '''
        return self.data['scheduledTask']

