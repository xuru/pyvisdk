
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineGuestSummary(DynamicData):
    '''A subset of virtual machine guest information.
    '''
    
    def __init__(self, guestFullName, guestId, hostName, ipAddress, toolsRunningStatus, toolsStatus, toolsVersionStatus):
        # MUST define these
        super(VirtualMachineGuestSummary, self).__init__()
    
        self.data['guestFullName'] = guestFullName
        self.data['guestId'] = guestId
        self.data['hostName'] = hostName
        self.data['ipAddress'] = ipAddress
        self.data['toolsRunningStatus'] = toolsRunningStatus
        self.data['toolsStatus'] = toolsStatus
        self.data['toolsVersionStatus'] = toolsVersionStatus
    
    
    @property
    def guestFullName(self):
        '''Guest operating system name configured on the virtual machine.
        '''
        return self.data['guestFullName']

    @property
    def guestId(self):
        '''Guest operating system identifier (short name), if known.
        '''
        return self.data['guestId']

    @property
    def hostName(self):
        '''Hostname of the guest operating system, if known.
        '''
        return self.data['hostName']

    @property
    def ipAddress(self):
        '''Primary IP address assigned to the guest operating system, if known.
        '''
        return self.data['ipAddress']

    @property
    def toolsRunningStatus(self):
        '''Current running status of VMware Tools in the guest operating system, if known.
        '''
        return self.data['toolsRunningStatus']

    @property
    def toolsStatus(self):
        '''Current status of VMware Tools in the guest operating system, if known.
        '''
        return self.data['toolsStatus']

    @property
    def toolsVersionStatus(self):
        '''Current version status of VMware Tools in the guest operating system, if known.
        '''
        return self.data['toolsVersionStatus']

