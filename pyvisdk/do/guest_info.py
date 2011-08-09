
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class GuestInfo(DynamicData):
    '''Information about the guest operating system.Most of this information is collected
        by VMware Tools. In general, be sure you have VMware Tools installed and
        that the virtual machine is running when you access this information.
    '''
    
    def __init__(self, appHeartbeatStatus, disk, guestFamily, guestFullName, guestId, guestState, hostName, ipAddress, ipStack, net, screen, toolsRunningStatus, toolsStatus, toolsVersion, toolsVersionStatus):
        # MUST define these
        super(GuestInfo, self).__init__()
    
        self.data['appHeartbeatStatus'] = appHeartbeatStatus
        self.data['disk'] = disk
        self.data['guestFamily'] = guestFamily
        self.data['guestFullName'] = guestFullName
        self.data['guestId'] = guestId
        self.data['guestState'] = guestState
        self.data['hostName'] = hostName
        self.data['ipAddress'] = ipAddress
        self.data['ipStack'] = ipStack
        self.data['net'] = net
        self.data['screen'] = screen
        self.data['toolsRunningStatus'] = toolsRunningStatus
        self.data['toolsStatus'] = toolsStatus
        self.data['toolsVersion'] = toolsVersion
        self.data['toolsVersionStatus'] = toolsVersionStatus
    
    
    @property
    def appHeartbeatStatus(self):
        '''Application heartbeat status. Please see VirtualMachineAppHeartbeatStatusType
        '''
        return self.data['appHeartbeatStatus']

    @property
    def disk(self):
        '''Guest information about disks, if known.
        '''
        return self.data['disk']

    @property
    def guestFamily(self):
        '''Guest operating system family, if known.
        '''
        return self.data['guestFamily']

    @property
    def guestFullName(self):
        '''Guest operating system full name, if known.
        '''
        return self.data['guestFullName']

    @property
    def guestId(self):
        '''Guest operating system identifier (short name), if known.
        '''
        return self.data['guestId']

    @property
    def guestState(self):
        '''Operation mode of guest operating system. One of: * "running" - Guest is running
        normally. * "shuttingdown" - Guest has a pending shutdown command. *
        "resetting" - Guest has a pending reset command. * "standby" - Guest has a
        pending standby command. * "notrunning" - Guest is not running. *
        "unknown" - Guest information is not available.
        '''
        return self.data['guestState']

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
    def ipStack(self):
        '''Guest information about IP networking stack, if known.
        '''
        return self.data['ipStack']

    @property
    def net(self):
        '''Guest information about network adapters, if known.
        '''
        return self.data['net']

    @property
    def screen(self):
        '''Guest screen resolution info, if known.
        '''
        return self.data['screen']

    @property
    def toolsRunningStatus(self):
        '''Current running status of VMware Tools in the guest operating system, if known.
        The set of possible values is described in
        VirtualMachineToolsRunningStatus
        '''
        return self.data['toolsRunningStatus']

    @property
    def toolsStatus(self):
        '''Current status of VMware Tools in the guest operating system, if known.
        '''
        return self.data['toolsStatus']

    @property
    def toolsVersion(self):
        '''Current version of VMware Tools, if known.
        '''
        return self.data['toolsVersion']

    @property
    def toolsVersionStatus(self):
        '''Current version status of VMware Tools in the guest operating system, if known.
        The set of possible values is described in
        VirtualMachineToolsVersionStatus
        '''
        return self.data['toolsVersionStatus']

