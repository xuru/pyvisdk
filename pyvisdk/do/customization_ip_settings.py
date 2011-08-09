
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationIPSettings(DynamicData):
    '''IP settings for a virtual network adapter.
    '''
    
    def __init__(self, dnsDomain, dnsServerList, gateway, ip, ipV6Spec, netBIOS, primaryWINS, secondaryWINS, subnetMask):
        # MUST define these
        super(CustomizationIPSettings, self).__init__()
    
        self.data['dnsDomain'] = dnsDomain
        self.data['dnsServerList'] = dnsServerList
        self.data['gateway'] = gateway
        self.data['ip'] = ip
        self.data['ipV6Spec'] = ipV6Spec
        self.data['netBIOS'] = netBIOS
        self.data['primaryWINS'] = primaryWINS
        self.data['secondaryWINS'] = secondaryWINS
        self.data['subnetMask'] = subnetMask
    
    
    @property
    def dnsDomain(self):
        '''A DNS domain suffix such as vmware.com.
        '''
        return self.data['dnsDomain']

    @property
    def dnsServerList(self):
        '''A list of server IP addresses to use for DNS lookup in a Windows guest operating
        system. In Windows, these settings are adapter-specific, whereas in Linux,
        they are global. As a result, the Linux guest customization process
        ignores this setting and looks for its DNS servers in the globalIPSettings
        object.
        '''
        return self.data['dnsServerList']

    @property
    def gateway(self):
        '''For a virtual network adapter with a static IP address, this data object type
        contains a list of gateways, in order of preference.
        '''
        return self.data['gateway']

    @property
    def ip(self):
        '''Specification to obtain a unique IP address for this virtual network adapter.
        '''
        return self.data['ip']

    @property
    def ipV6Spec(self):
        '''This contains the IpGenerator, subnet mask and gateway info for all the ipv6
        addresses associated with the virtual network adapter.
        '''
        return self.data['ipV6Spec']

    @property
    def netBIOS(self):
        '''NetBIOS setting for Windows.
        '''
        return self.data['netBIOS']

    @property
    def primaryWINS(self):
        '''The IP address of the primary WINS server. This property is ignored for Linux
        guest operating systems.
        '''
        return self.data['primaryWINS']

    @property
    def secondaryWINS(self):
        '''The IP address of the secondary WINS server. This property is ignored for Linux
        guest operating systems.
        '''
        return self.data['secondaryWINS']

    @property
    def subnetMask(self):
        '''Subnet mask for this virtual network adapter.
        '''
        return self.data['subnetMask']

