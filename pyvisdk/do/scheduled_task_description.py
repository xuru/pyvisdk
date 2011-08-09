
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ScheduledTaskDescription(DynamicData):
    '''Static strings for scheduled tasks. These strings are locale-specific.
    '''
    
    def __init__(self, action, dayOfWeek, schedulerInfo, state, weekOfMonth):
        # MUST define these
        super(ScheduledTaskDescription, self).__init__()
    
        self.data['action'] = action
        self.data['dayOfWeek'] = dayOfWeek
        self.data['schedulerInfo'] = schedulerInfo
        self.data['state'] = state
        self.data['weekOfMonth'] = weekOfMonth
    
    
    @property
    def action(self):
        '''Action class descriptions for a scheduled task.
        '''
        return self.data['action']

    @property
    def dayOfWeek(self):
        '''MonthlyByWeekdayTaskScheduler Days of the week enum description
        '''
        return self.data['dayOfWeek']

    @property
    def schedulerInfo(self):
        '''Scheduler class description details.
        '''
        return self.data['schedulerInfo']

    @property
    def state(self):
        '''TaskInfo State enum
        '''
        return self.data['state']

    @property
    def weekOfMonth(self):
        '''MonthlyByWeekdayTaskScheduler Week of the month enum description
        '''
        return self.data['weekOfMonth']

