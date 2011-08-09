
from pyvisdk.do.entity_event_argument import EntityEventArgument
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AlarmEventArgument(EntityEventArgument):
    '''The event argument is an Alarm object.
    '''
    
    def __init__(self, alarm):
        # MUST define these
        super(AlarmEventArgument, self).__init__()
    
        self.data['alarm'] = alarm
    
    
    @property
    def alarm(self):
        '''The Alarm object.
        '''
        return self.data['alarm']

