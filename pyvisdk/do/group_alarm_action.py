
from pyvisdk.do.alarm_action import AlarmAction
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class GroupAlarmAction(AlarmAction):
    '''This data object type describes a group of actions that occur when the alarm is
        triggered. These actions are not necessarily executed in order.
    '''
    
    def __init__(self, action):
        # MUST define these
        super(GroupAlarmAction, self).__init__()
    
        self.data['action'] = action
    
    
    @property
    def action(self):
        '''The list of alarm actions that occur when the alarm is triggered.
        '''
        return self.data['action']

