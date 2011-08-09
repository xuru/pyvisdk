
from pyvisdk.do.apply_profile import ApplyProfile
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NetworkProfile(ApplyProfile):
    '''DataObject represents a profile for network configuration.
    '''
    
    def __init__(self, consoleIpRouteConfig, dnsConfig, dvsHostNic, dvsServiceConsoleNic, dvswitch, hostPortGroup, ipRouteConfig, pnic, serviceConsolePortGroup, vmPortGroup, vswitch):
        # MUST define these
        super(NetworkProfile, self).__init__()
    
        self.data['consoleIpRouteConfig'] = consoleIpRouteConfig
        self.data['dnsConfig'] = dnsConfig
        self.data['dvsHostNic'] = dvsHostNic
        self.data['dvsServiceConsoleNic'] = dvsServiceConsoleNic
        self.data['dvswitch'] = dvswitch
        self.data['hostPortGroup'] = hostPortGroup
        self.data['ipRouteConfig'] = ipRouteConfig
        self.data['pnic'] = pnic
        self.data['serviceConsolePortGroup'] = serviceConsolePortGroup
        self.data['vmPortGroup'] = vmPortGroup
        self.data['vswitch'] = vswitch
    
    
    @property
    def consoleIpRouteConfig(self):
        '''Profile representing the Ip Route configuration for the Service Console gateway.
        '''
        return self.data['consoleIpRouteConfig']

    @property
    def dnsConfig(self):
        '''Profile representing the DNS configuration
        '''
        return self.data['dnsConfig']

    @property
    def dvsHostNic(self):
        '''List of Host Vnics connected to a Distributed Virtual Switch
        '''
        return self.data['dvsHostNic']

    @property
    def dvsServiceConsoleNic(self):
        '''List of Service Console Vnics connected to a Distributed Virtual Switch
        '''
        return self.data['dvsServiceConsoleNic']

    @property
    def dvswitch(self):
        '''Distributed Virtual Switches which this host is part of
        '''
        return self.data['dvswitch']

    @property
    def hostPortGroup(self):
        '''The set of portgroups for use by the Host
        '''
        return self.data['hostPortGroup']

    @property
    def ipRouteConfig(self):
        '''Profile representing the Ip Route configuration for the VMKernel gateway.
        '''
        return self.data['ipRouteConfig']

    @property
    def pnic(self):
        '''Profile representing the Physical Nic configurations.
        '''
        return self.data['pnic']

    @property
    def serviceConsolePortGroup(self):
        '''The set of portgroups for use by Service Console. This field is considered only
        when applying the profile on hosts which have a ServiceConsole.
        '''
        return self.data['serviceConsolePortGroup']

    @property
    def vmPortGroup(self):
        '''The set of portgroups for use by Virtual Machines
        '''
        return self.data['vmPortGroup']

    @property
    def vswitch(self):
        '''The set of virtual switches.
        '''
        return self.data['vswitch']

