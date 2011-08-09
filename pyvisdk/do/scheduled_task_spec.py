
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ScheduledTaskSpec(DynamicData):
    '''Parameters for scheduled task creation.
    '''
    
    def __init__(self, action, description, enabled, name, notification, scheduler):
        # MUST define these
        super(ScheduledTaskSpec, self).__init__()
    
        self.data['action'] = action
        self.data['description'] = description
        self.data['enabled'] = enabled
        self.data['name'] = name
        self.data['notification'] = notification
        self.data['scheduler'] = scheduler
    
    
    @property
    def action(self):
        '''The action of the scheduled task, to be done when the scheduled task runs.
        '''
        return self.data['action']

    @property
    def description(self):
        '''Description of the scheduled task.
        '''
        return self.data['description']

    @property
    def enabled(self):
        '''Flag to indicate whether the scheduled task is enabled or disabled.
        '''
        return self.data['enabled']

    @property
    def name(self):
        '''Name of the scheduled task.
        '''
        return self.data['name']

    @property
    def notification(self):
        '''The email notification. If not set, this property is set to empty string,
        indicating no notification.
        '''
        return self.data['notification']

    @property
    def scheduler(self):
        '''The time scheduler that determines when the scheduled task runs.
        '''
        return self.data['scheduler']

