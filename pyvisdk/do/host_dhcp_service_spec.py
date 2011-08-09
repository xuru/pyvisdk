
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDhcpServiceSpec(DynamicData):
    '''
    '''
    
    def __init__(self, defaultLeaseDuration, ipSubnetAddr, ipSubnetMask, leaseBeginIp, leaseEndIp, maxLeaseDuration, unlimitedLease, virtualSwitch):
        # MUST define these
        super(HostDhcpServiceSpec, self).__init__()
    
        self.data['defaultLeaseDuration'] = defaultLeaseDuration
        self.data['ipSubnetAddr'] = ipSubnetAddr
        self.data['ipSubnetMask'] = ipSubnetMask
        self.data['leaseBeginIp'] = leaseBeginIp
        self.data['leaseEndIp'] = leaseEndIp
        self.data['maxLeaseDuration'] = maxLeaseDuration
        self.data['unlimitedLease'] = unlimitedLease
        self.data['virtualSwitch'] = virtualSwitch
    
    
    @property
    def defaultLeaseDuration(self):
        '''The default DHCP lease duration (minutes).
        '''
        return self.data['defaultLeaseDuration']

    @property
    def ipSubnetAddr(self):
        '''Subnet served by DHCP service.
        '''
        return self.data['ipSubnetAddr']

    @property
    def ipSubnetMask(self):
        '''Subnet mask of network served by DHCP service.
        '''
        return self.data['ipSubnetMask']

    @property
    def leaseBeginIp(self):
        '''The start of the IP address range served by the DHCP service.
        '''
        return self.data['leaseBeginIp']

    @property
    def leaseEndIp(self):
        '''The end of the IP address range served by the DHCP service.
        '''
        return self.data['leaseEndIp']

    @property
    def maxLeaseDuration(self):
        '''The maximum DHCP lease duration (minutes).
        '''
        return self.data['maxLeaseDuration']

    @property
    def unlimitedLease(self):
        '''A flag to indicate whether or not unlimited DHCP lease durations are allowed.
        '''
        return self.data['unlimitedLease']

    @property
    def virtualSwitch(self):
        '''The name of the virtual switch to which DHCP service is connected.
        '''
        return self.data['virtualSwitch']

