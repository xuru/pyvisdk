
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostIpmiInfo(DynamicData):
    '''The IpmiInfo data object contains IPMI (Intelligent Platform Management Interface)
        and BMC (Baseboard Management Controller) information for the host.
    '''
    
    def __init__(self, bmcIpAddress, bmcMacAddress, login, password):
        # MUST define these
        super(HostIpmiInfo, self).__init__()
    
        self.data['bmcIpAddress'] = bmcIpAddress
        self.data['bmcMacAddress'] = bmcMacAddress
        self.data['login'] = login
        self.data['password'] = password
    
    
    @property
    def bmcIpAddress(self):
        '''IP address of the BMC on the host. It should be null terminated.
        '''
        return self.data['bmcIpAddress']

    @property
    def bmcMacAddress(self):
        '''MAC address of the BMC on the host. The MAC address should be of the form
        xx:xx:xx:xx:xx:xx where each x is a hex digit. It should be null
        terminated.
        '''
        return self.data['bmcMacAddress']

    @property
    def login(self):
        '''User ID for logging into the BMC. BMC usernames may be up to 16 characters and
        must be null terminated. Hence, a login comprises 17 or fewer characters.
        '''
        return self.data['login']

    @property
    def password(self):
        '''Password for logging into the BMC. Only used for configuration, returned as unset
        while reading. The password can be up to 16 characters and must be null
        terminated. Hence, a password comprises 17 or fewer characters.
        '''
        return self.data['password']

