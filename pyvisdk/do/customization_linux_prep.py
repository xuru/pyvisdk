
from pyvisdk.do.customization_identity_settings import CustomizationIdentitySettings
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationLinuxPrep(CustomizationIdentitySettings):
    '''This is the Linux counterpart to the Windows Sysprep object. LinuxPrep contains
        machine-wide settings that identify a Linux machine in the same way that
        the Sysprep type identifies a Windows machine.
    '''
    
    def __init__(self, domain, hostName, hwClockUTC, timeZone):
        # MUST define these
        super(CustomizationLinuxPrep, self).__init__()
    
        self.data['domain'] = domain
        self.data['hostName'] = hostName
        self.data['hwClockUTC'] = hwClockUTC
        self.data['timeZone'] = timeZone
    
    
    @property
    def domain(self):
        '''The fully qualified domain name.
        '''
        return self.data['domain']

    @property
    def hostName(self):
        '''The network host name of the (Linux) virtual machine.
        '''
        return self.data['hostName']

    @property
    def hwClockUTC(self):
        '''Specifies whether the hardware clock is in UTC or local time. * True when the
        hardware clock is in UTC. * False when the hardware clock is in local
        time.
        '''
        return self.data['hwClockUTC']

    @property
    def timeZone(self):
        '''The case-sensitive timezone, such as Europe/Sofia.
        '''
        return self.data['timeZone']

