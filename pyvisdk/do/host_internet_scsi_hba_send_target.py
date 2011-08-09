
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostInternetScsiHbaSendTarget(DynamicData):
    '''The iSCSI send target.
    '''
    
    def __init__(self, address, advancedOptions, authenticationProperties, digestProperties, parent, port, supportedAdvancedOptions):
        # MUST define these
        super(HostInternetScsiHbaSendTarget, self).__init__()
    
        self.data['address'] = address
        self.data['advancedOptions'] = advancedOptions
        self.data['authenticationProperties'] = authenticationProperties
        self.data['digestProperties'] = digestProperties
        self.data['parent'] = parent
        self.data['port'] = port
        self.data['supportedAdvancedOptions'] = supportedAdvancedOptions
    
    
    @property
    def address(self):
        '''The IP address or hostname of the storage device.
        '''
        return self.data['address']

    @property
    def advancedOptions(self):
        '''A list of the current options settings for the host bus adapter.
        '''
        return self.data['advancedOptions']

    @property
    def authenticationProperties(self):
        '''The authentication settings for this discovery target. All static targets
        discovered via this target will inherit the use of these settings unless
        the static target's authentication settings are explicitly set.
        '''
        return self.data['authenticationProperties']

    @property
    def digestProperties(self):
        '''The digest settings for this discovery target. All static targets discovered via
        this target will inherit the use of these settings unless the static
        target's digest settings are explicitly set.
        '''
        return self.data['digestProperties']

    @property
    def parent(self):
        '''The device name of the host bus adapter from which settings can be inherited.
        '''
        return self.data['parent']

    @property
    def port(self):
        '''The TCP port of the storage device. If not specified, the standard default of 3260
        is used.
        '''
        return self.data['port']

    @property
    def supportedAdvancedOptions(self):
        '''A list of supported key/value pair advanced options for the host bus adapter
        including their type information.
        '''
        return self.data['supportedAdvancedOptions']

