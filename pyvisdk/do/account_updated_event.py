
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AccountUpdatedEvent(HostEvent):
    '''This event records that an account was updated on a host.
    '''
    
    def __init__(self, group, spec):
        # MUST define these
        super(AccountUpdatedEvent, self).__init__()
    
        self.data['group'] = group
        self.data['spec'] = spec
    
    
    @property
    def group(self):
        '''
        '''
        return self.data['group']

    @property
    def spec(self):
        '''
        '''
        return self.data['spec']
