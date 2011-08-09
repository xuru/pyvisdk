
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDateTimeSystemTimeZone(DynamicData):
    '''
    '''
    
    def __init__(self, description, gmtOffset, key, name):
        # MUST define these
        super(HostDateTimeSystemTimeZone, self).__init__()
    
        self.data['description'] = description
        self.data['gmtOffset'] = gmtOffset
        self.data['key'] = key
        self.data['name'] = name
    
    
    @property
    def description(self):
        '''Description of the time zone.
        '''
        return self.data['description']

    @property
    def gmtOffset(self):
        '''The GMT offset in seconds that is currently applicable to the timezone (with
        respect to the current time on the host).
        '''
        return self.data['gmtOffset']

    @property
    def key(self):
        '''The identifier for the time zone.
        '''
        return self.data['key']

    @property
    def name(self):
        '''The time zone name.
        '''
        return self.data['name']

