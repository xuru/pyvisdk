
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostWwnConflictEvent(HostEvent):
    '''This event records a conflict of host WWNs (World Wide Name).
    '''
    
    def __init__(self, conflictedHosts, conflictedVms, wwn):
        # MUST define these
        super(HostWwnConflictEvent, self).__init__()
    
        self.data['conflictedHosts'] = conflictedHosts
        self.data['conflictedVms'] = conflictedVms
        self.data['wwn'] = wwn
    
    
    @property
    def conflictedHosts(self):
        '''The host whose physical WWN conflicts with the current host's WWN.
        '''
        return self.data['conflictedHosts']

    @property
    def conflictedVms(self):
        '''The virtual machine whose WWN conflicts with the current host's WWN.
        '''
        return self.data['conflictedVms']

    @property
    def wwn(self):
        '''The WWN in conflict.
        '''
        return self.data['wwn']

