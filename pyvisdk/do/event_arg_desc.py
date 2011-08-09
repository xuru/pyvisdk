
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class EventArgDesc(DynamicData):
    '''Describes an available event argument name for an Event type, which can be used in
        EventAlarmExpression.
    '''
    
    def __init__(self, description, name, type):
        # MUST define these
        super(EventArgDesc, self).__init__()
    
        self.data['description'] = description
        self.data['name'] = name
        self.data['type'] = type
    
    
    @property
    def description(self):
        '''The localized description of the event argument. The key holds the localization
        prefix for the argument, which is decided by the Event type that it is
        actually declared in, which may be a base type of this event type.
        '''
        return self.data['description']

    @property
    def name(self):
        '''The name of the argument
        '''
        return self.data['name']

    @property
    def type(self):
        '''The type of the argument. The supported values are
        '''
        return self.data['type']

