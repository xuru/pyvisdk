
from pyvisdk.do.license_event import LicenseEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AllVirtualMachinesLicensedEvent(LicenseEvent):
    '''This event records that the previously unlicensed virtual machines on the
        specified host are now licensed. After this event is entered into the
        event log, we expect to see that the (@link
        vim.event.Event.UnlicensedVirtualMachinesEvent
        UnlicensedVirtualMachinesEvent) (@link vim.ManagedEntity.configIssue
        configIssue) is removed from the host.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(AllVirtualMachinesLicensedEvent, self).__init__()
    

    
    
