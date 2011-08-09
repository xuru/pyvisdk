
from pyvisdk.do.license_event import LicenseEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class UnlicensedVirtualMachinesFoundEvent(LicenseEvent):
    '''This event records that we discovered unlicensed virtual machines on the specified
        host. After this event is entered into the event log, we expect to see a
        corresponding (@link vim.event.Event.UnlicensedVirtualMachinesEvent
        UnlicensedVirtualMachinesEvent) (@link vim.ManagedEntity.configIssue
        configIssue) on the host.
    '''
    
    def __init__(self, available):
        # MUST define these
        super(UnlicensedVirtualMachinesFoundEvent, self).__init__()
    
        self.data['available'] = available
    
    
    @property
    def available(self):
        '''
        '''
        return self.data['available']

