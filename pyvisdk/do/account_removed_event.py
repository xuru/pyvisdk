
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AccountRemovedEvent(HostEvent):
    '''This event records that an account was removed from a host.
    '''
    
    def __init__(self, account, group):
        # MUST define these
        super(AccountRemovedEvent, self).__init__()
    
        self.data['account'] = account
        self.data['group'] = group
    
    
    @property
    def account(self):
        '''
        '''
        return self.data['account']

    @property
    def group(self):
        '''
        '''
        return self.data['group']

