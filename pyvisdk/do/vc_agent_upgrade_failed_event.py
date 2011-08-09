
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VcAgentUpgradeFailedEvent(HostEvent):
    '''This event records when the VirtualCenter agent on a host failed to upgrade.
    '''
    
    def __init__(self, reason):
        # MUST define these
        super(VcAgentUpgradeFailedEvent, self).__init__()
    
        self.data['reason'] = reason
    
    
    @property
    def reason(self):
        '''The reason why the upgrade failed, if known. See AgentInstallFailedReason
        '''
        return self.data['reason']

