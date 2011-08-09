
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AlarmSpec(DynamicData):
    '''Parameters for alarm creation.
    '''
    
    def __init__(self, action, actionFrequency, description, enabled, expression, name, setting):
        # MUST define these
        super(AlarmSpec, self).__init__()
    
        self.data['action'] = action
        self.data['actionFrequency'] = actionFrequency
        self.data['description'] = description
        self.data['enabled'] = enabled
        self.data['expression'] = expression
        self.data['name'] = name
        self.data['setting'] = setting
    
    
    @property
    def action(self):
        '''Action to perform when the alarm is triggered.
        '''
        return self.data['action']

    @property
    def actionFrequency(self):
        '''Frequency in seconds, which specifies how often appropriate actions should repeat
        when an alarm does not change state.
        '''
        return self.data['actionFrequency']

    @property
    def description(self):
        '''Description of the alarm.
        '''
        return self.data['description']

    @property
    def enabled(self):
        '''Flag to indicate whether or not the alarm is enabled or disabled.
        '''
        return self.data['enabled']

    @property
    def expression(self):
        '''Top-level alarm expression that defines trigger conditions.
        '''
        return self.data['expression']

    @property
    def name(self):
        '''Name of the alarm.
        '''
        return self.data['name']

    @property
    def setting(self):
        '''Tolerance and maximum frequency settings.
        '''
        return self.data['setting']

