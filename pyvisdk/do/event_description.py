
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class EventDescription(DynamicData):
    '''This data object provides static, locale-specific strings for event objects.
    '''
    
    def __init__(self, category, enumeratedTypes, eventInfo):
        # MUST define these
        super(EventDescription, self).__init__()
    
        self.data['category'] = category
        self.data['enumeratedTypes'] = enumeratedTypes
        self.data['eventInfo'] = eventInfo
    
    
    @property
    def category(self):
        '''Event Category enum
        '''
        return self.data['category']

    @property
    def enumeratedTypes(self):
        '''Localized descriptions of all enumerated types that are used for member
        declarations in event classes.
        '''
        return self.data['enumeratedTypes']

    @property
    def eventInfo(self):
        '''The event class description details.
        '''
        return self.data['eventInfo']

