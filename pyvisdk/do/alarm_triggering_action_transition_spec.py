
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AlarmTriggeringActionTransitionSpec(DynamicData):
    '''Specification indicating which on transitions this action fires. The existence of
        a Spec indicates that this action fires on transitions from that Spec's
        startState to finalState.There are only four acceptable {startState,
        finalState} pairs: {green, yellow}, {yellow, red}, {red, yellow} and
        {yellow, green}. At least one of these pairs must be specified. Any
        deviation from the above will render the enclosing AlarmSpec invalid.
    '''
    
    def __init__(self, finalState, repeats, startState):
        # MUST define these
        super(AlarmTriggeringActionTransitionSpec, self).__init__()
    
        self.data['finalState'] = finalState
        self.data['repeats'] = repeats
        self.data['startState'] = startState
    
    
    @property
    def finalState(self):
        '''The state to which the alarm must transition for the action to fire. Valid choices
        are red, yellow, and green.
        '''
        return self.data['finalState']

    @property
    def repeats(self):
        '''Whether or not the action repeats, as per the actionFrequency defined in the
        enclosing Alarm.
        '''
        return self.data['repeats']

    @property
    def startState(self):
        '''The state from which the alarm must transition for the action to fire. Valid
        choices are red, yellow and green.
        '''
        return self.data['startState']

