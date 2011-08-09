
from pyvisdk.do.entity_event_argument import EntityEventArgument
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostEventArgument(EntityEventArgument):
    '''The event argument is a Host object.
    '''
    
    def __init__(self, host):
        # MUST define these
        super(HostEventArgument, self).__init__()
    
        self.data['host'] = host
    
    
    @property
    def host(self):
        '''The host object.
        '''
        return self.data['host']

