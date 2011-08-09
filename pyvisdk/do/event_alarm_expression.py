
from pyvisdk.do.alarm_expression import AlarmExpression
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class EventAlarmExpression(AlarmExpression):
    '''An alarm expression that uses the event stream to trigger the alarm.This alarm is
        triggered when an event matching this expression gets logged.
    '''
    
    def __init__(self, comparisons, eventType, eventTypeId, objectType, status):
        # MUST define these
        super(EventAlarmExpression, self).__init__()
    
        self.data['comparisons'] = comparisons
        self.data['eventType'] = eventType
        self.data['eventTypeId'] = eventTypeId
        self.data['objectType'] = objectType
        self.data['status'] = status
    
    
    @property
    def comparisons(self):
        '''The attributes/values to compare.
        '''
        return self.data['comparisons']

    @property
    def eventType(self):
        '''The type of the event to trigger the alarm on.
        '''
        return self.data['eventType']

    @property
    def eventTypeId(self):
        '''The eventTypeId of the event to match.
        '''
        return self.data['eventTypeId']

    @property
    def objectType(self):
        '''Name of the type of managed object on which the event is logged.
        '''
        return self.data['objectType']

    @property
    def status(self):
        '''The alarm's new state when this condition is evaluated and satisfied. If not
        specified then there is no change to alarm status, and all actions are
        fired (rather than those for the transition).
        '''
        return self.data['status']

