
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostListSummary(DynamicData):
    '''This data object type encapsulates a typical set of host information that is
        useful for list views and summary pages.VirtualCenter can retrieve this
        information very efficiently, even for a large set of hosts.
    '''
    
    def __init__(self, config, currentEVCModeKey, customValue, hardware, host, managementServerIp, maxEVCModeKey, overallStatus, quickStats, rebootRequired, runtime):
        # MUST define these
        super(HostListSummary, self).__init__()
    
        self.data['config'] = config
        self.data['currentEVCModeKey'] = currentEVCModeKey
        self.data['customValue'] = customValue
        self.data['hardware'] = hardware
        self.data['host'] = host
        self.data['managementServerIp'] = managementServerIp
        self.data['maxEVCModeKey'] = maxEVCModeKey
        self.data['overallStatus'] = overallStatus
        self.data['quickStats'] = quickStats
        self.data['rebootRequired'] = rebootRequired
        self.data['runtime'] = runtime
    
    
    @property
    def config(self):
        '''Basic configuration information, if known.
        '''
        return self.data['config']

    @property
    def currentEVCModeKey(self):
        '''The Enhanced VMotion Compatibility mode that is currently in effect for this host.
        If the host is in a cluster where EVC is active, this will match the
        cluster's EVC mode; otherwise this will be unset.
        '''
        return self.data['currentEVCModeKey']

    @property
    def customValue(self):
        '''The customized field values.
        '''
        return self.data['customValue']

    @property
    def hardware(self):
        '''Basic hardware information, if known.
        '''
        return self.data['hardware']

    @property
    def host(self):
        '''The reference to the host-managed object.
        '''
        return self.data['host']

    @property
    def managementServerIp(self):
        '''IP address of the VirtualCenter server managing this host, if any.
        '''
        return self.data['managementServerIp']

    @property
    def maxEVCModeKey(self):
        '''The most capable Enhanced VMotion Compatibility mode supported by the host
        hardware and software; unset if this host cannot participate in any EVC
        mode.
        '''
        return self.data['maxEVCModeKey']

    @property
    def overallStatus(self):
        '''The overall alarm status of the host.
        '''
        return self.data['overallStatus']

    @property
    def quickStats(self):
        '''Basic host statistics.
        '''
        return self.data['quickStats']

    @property
    def rebootRequired(self):
        '''Indicates whether or not the host requires a reboot due to a configuration change.
        '''
        return self.data['rebootRequired']

    @property
    def runtime(self):
        '''Basic runtime information, if known.
        '''
        return self.data['runtime']

