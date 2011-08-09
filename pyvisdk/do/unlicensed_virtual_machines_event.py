
from pyvisdk.do.license_event import LicenseEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class UnlicensedVirtualMachinesEvent(LicenseEvent):
    '''This event records that we have unlicensed virtual machines on the specified host.
        This can be both a (@link vim.ManagedEntity.configIssue configIssue) and
        an entry in the event log.
    '''
    
    def __init__(self, available, unlicensed):
        # MUST define these
        super(UnlicensedVirtualMachinesEvent, self).__init__()
    
        self.data['available'] = available
        self.data['unlicensed'] = unlicensed
    
    
    @property
    def available(self):
        '''
        '''
        return self.data['available']

    @property
    def unlicensed(self):
        '''
        '''
        return self.data['unlicensed']

