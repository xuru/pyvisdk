
from pyvisdk.do.alarm_action import AlarmAction
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AlarmTriggeringAction(AlarmAction):
    '''This data object type describes one or more triggering transitions and an action
        to be done when an alarm is triggered.There are four triggering
        transitions; at least one of them must be provided. A gray state is
        considered the same as a green state, for the purpose of detecting
        transitions.
    '''
    
    def __init__(self, action, green2yellow, red2yellow, transitionSpecs, yellow2green, yellow2red):
        # MUST define these
        super(AlarmTriggeringAction, self).__init__()
    
        self.data['action'] = action
        self.data['green2yellow'] = green2yellow
        self.data['red2yellow'] = red2yellow
        self.data['transitionSpecs'] = transitionSpecs
        self.data['yellow2green'] = yellow2green
        self.data['yellow2red'] = yellow2red
    
    
    @property
    def action(self):
        '''The action to be done when the alarm is triggered.
        '''
        return self.data['action']

    @property
    def green2yellow(self):
        '''Flag to specify that the alarm should trigger on a transition from green to
        yellow.
        '''
        return self.data['green2yellow']

    @property
    def red2yellow(self):
        '''Flag to specify that the alarm should trigger on a transition from red to yellow.
        '''
        return self.data['red2yellow']

    @property
    def transitionSpecs(self):
        '''Indicates on which transitions this action executes and repeats. This is optional
        only for backwards compatibility.
        '''
        return self.data['transitionSpecs']

    @property
    def yellow2green(self):
        '''Flag to specify that the alarm should trigger on a transition from yellow to
        green.
        '''
        return self.data['yellow2green']

    @property
    def yellow2red(self):
        '''Flag to specify that the alarm should trigger on a transition from yellow to red.
        '''
        return self.data['yellow2red']

