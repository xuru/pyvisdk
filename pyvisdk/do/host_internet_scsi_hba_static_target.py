
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostInternetScsiHbaStaticTarget(DynamicData):
    '''The iSCSI static target.
    '''
    
    def __init__(self, address, advancedOptions, authenticationProperties, digestProperties, iScsiName, parent, port, supportedAdvancedOptions):
        # MUST define these
        super(HostInternetScsiHbaStaticTarget, self).__init__()
    
        self.data['address'] = address
        self.data['advancedOptions'] = advancedOptions
        self.data['authenticationProperties'] = authenticationProperties
        self.data['digestProperties'] = digestProperties
        self.data['iScsiName'] = iScsiName
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
        '''The authentication settings for this target.
        '''
        return self.data['authenticationProperties']

    @property
    def digestProperties(self):
        '''The digest settings for this target.
        '''
        return self.data['digestProperties']

    @property
    def iScsiName(self):
        '''The iSCSI name of the storage device.
        '''
        return self.data['iScsiName']

    @property
    def parent(self):
        '''The parent entity from which settings can be inherited. It can either be unset, or
        set to the device name of the host bus adapter or the name of the
        SendTarget.
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

