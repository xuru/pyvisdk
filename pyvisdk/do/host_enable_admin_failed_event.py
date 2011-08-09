
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostEnableAdminFailedEvent(HostEvent):
    '''This event records the failure to restore some of the administrator's permissions.
    '''
    
    def __init__(self, permissions):
        # MUST define these
        super(HostEnableAdminFailedEvent, self).__init__()
    
        self.data['permissions'] = permissions
    
    
    @property
    def permissions(self):
        '''
        '''
        return self.data['permissions']

