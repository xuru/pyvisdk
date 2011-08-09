
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationGlobalIPSettings(DynamicData):
    '''A collection of global IP settings for a virtual network adapter. In Linux, DNS
        server settings are global. The settings can either be statically set or
        supplied by a DHCP server.
    '''
    
    def __init__(self, dnsServerList, dnsSuffixList):
        # MUST define these
        super(CustomizationGlobalIPSettings, self).__init__()
    
        self.data['dnsServerList'] = dnsServerList
        self.data['dnsSuffixList'] = dnsSuffixList
    
    
    @property
    def dnsServerList(self):
        '''List of DNS servers, for a virtual network adapter with a static IP address. If
        this list is empty, then the guest operating system is expected to use a
        DHCP server to get its DNS server settings. These settings configure the
        virtual machine to use the specified DNS servers. These DNS server
        settings are listed in order of preference.
        '''
        return self.data['dnsServerList']

    @property
    def dnsSuffixList(self):
        '''List of name resolution suffixes for the virtual network adapter. This list
        applies to both Windows and Linux guest customization. For Linux, this
        setting is global, whereas in Windows, this setting is listed on a per-
        adapter basis, even though the setting is global in Windows.
        '''
        return self.data['dnsSuffixList']

