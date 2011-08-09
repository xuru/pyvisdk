
from pyvisdk.do.event import Event
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AlarmEvent(Event):
    '''This event is an alarm events.
    '''
    
    def __init__(self, alarm):
        # MUST define these
        super(AlarmEvent, self).__init__()
    
        self.data['alarm'] = alarm
    
    
    @property
    def alarm(self):
        '''The associated alarm object.
        '''
        return self.data['alarm']

