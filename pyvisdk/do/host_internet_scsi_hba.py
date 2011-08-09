
from pyvisdk.do.host_host_bus_adapter import HostHostBusAdapter
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostInternetScsiHba(HostHostBusAdapter):
    '''This data object type describes the iSCSI host bus adapter interface.
    '''
    
    def __init__(self, advancedOptions, authenticationCapabilities, authenticationProperties, configuredSendTarget, configuredStaticTarget, currentSpeedMb, digestCapabilities, digestProperties, discoveryCapabilities, discoveryProperties, ipCapabilities, ipProperties, iScsiAlias, iScsiName, isSoftwareBased, maxSpeedMb, supportedAdvancedOptions):
        # MUST define these
        super(HostInternetScsiHba, self).__init__()
    
        self.data['advancedOptions'] = advancedOptions
        self.data['authenticationCapabilities'] = authenticationCapabilities
        self.data['authenticationProperties'] = authenticationProperties
        self.data['configuredSendTarget'] = configuredSendTarget
        self.data['configuredStaticTarget'] = configuredStaticTarget
        self.data['currentSpeedMb'] = currentSpeedMb
        self.data['digestCapabilities'] = digestCapabilities
        self.data['digestProperties'] = digestProperties
        self.data['discoveryCapabilities'] = discoveryCapabilities
        self.data['discoveryProperties'] = discoveryProperties
        self.data['ipCapabilities'] = ipCapabilities
        self.data['ipProperties'] = ipProperties
        self.data['iScsiAlias'] = iScsiAlias
        self.data['iScsiName'] = iScsiName
        self.data['isSoftwareBased'] = isSoftwareBased
        self.data['maxSpeedMb'] = maxSpeedMb
        self.data['supportedAdvancedOptions'] = supportedAdvancedOptions
    
    
    @property
    def advancedOptions(self):
        '''A list of the current options settings for the host bus adapter.
        '''
        return self.data['advancedOptions']

    @property
    def authenticationCapabilities(self):
        '''The authentication capabilities for this host bus adapter.
        '''
        return self.data['authenticationCapabilities']

    @property
    def authenticationProperties(self):
        '''The authentication settings for this host bus adapter. All static and discovery
        targets will inherit the use of these settings unless their authentication
        settings are explicitly set.
        '''
        return self.data['authenticationProperties']

    @property
    def configuredSendTarget(self):
        '''The configured iSCSI send target entries.
        '''
        return self.data['configuredSendTarget']

    @property
    def configuredStaticTarget(self):
        '''The configured iSCSI static target entries.
        '''
        return self.data['configuredStaticTarget']

    @property
    def currentSpeedMb(self):
        '''The Current operating link speed of the port in megabits per second.
        '''
        return self.data['currentSpeedMb']

    @property
    def digestCapabilities(self):
        '''The authentication capabilities for this host bus adapter.
        '''
        return self.data['digestCapabilities']

    @property
    def digestProperties(self):
        '''The digest settings for this host bus adapter. All static and discovery targets
        will inherit the use of these properties unless their digest settings are
        explicitly set.
        '''
        return self.data['digestProperties']

    @property
    def discoveryCapabilities(self):
        '''The discovery capabilities for this host bus adapter.
        '''
        return self.data['discoveryCapabilities']

    @property
    def discoveryProperties(self):
        '''The discovery settings for this host bus adapter.
        '''
        return self.data['discoveryProperties']

    @property
    def ipCapabilities(self):
        '''The IP capabilities for this host bus adapter.
        '''
        return self.data['ipCapabilities']

    @property
    def ipProperties(self):
        '''The IP settings for this host bus adapter.
        '''
        return self.data['ipProperties']

    @property
    def iScsiAlias(self):
        '''The iSCSI alias of this host bus adapter.
        '''
        return self.data['iScsiAlias']

    @property
    def iScsiName(self):
        '''The iSCSI name of this host bus adapter.
        '''
        return self.data['iScsiName']

    @property
    def isSoftwareBased(self):
        '''True if this host bus adapter is a software based initiator utilizing the hosting
        system's existing TCP/IP network connection
        '''
        return self.data['isSoftwareBased']

    @property
    def maxSpeedMb(self):
        '''The maximum supported link speed of the port in megabits per second.
        '''
        return self.data['maxSpeedMb']

    @property
    def supportedAdvancedOptions(self):
        '''A list of supported key/value pair advanced options for the host bus adapter
        including their type information.
        '''
        return self.data['supportedAdvancedOptions']

