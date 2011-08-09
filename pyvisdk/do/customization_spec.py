
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationSpec(DynamicData):
    '''The Specification data object type contains information required to customize a
        virtual machine when deploying it or migrating it to a new host.
    '''
    
    def __init__(self, encryptionKey, globalIPSettings, identity, nicSettingMap, options):
        # MUST define these
        super(CustomizationSpec, self).__init__()
    
        self.data['encryptionKey'] = encryptionKey
        self.data['globalIPSettings'] = globalIPSettings
        self.data['identity'] = identity
        self.data['nicSettingMap'] = nicSettingMap
        self.data['options'] = options
    
    
    @property
    def encryptionKey(self):
        '''Byte array containing the public key used to encrypt any passwords stored in the
        specification. Both the client and the server can use this to determine if
        stored passwords can be decrypted by the server or if the passwords need
        to be re-entered and re-encrypted before the specification can be used.
        '''
        return self.data['encryptionKey']

    @property
    def globalIPSettings(self):
        '''Global IP settings constitute the IP settings that are not specific to a
        particular virtual network adapter.
        '''
        return self.data['globalIPSettings']

    @property
    def identity(self):
        '''Network identity and settings, similar to Microsoft's Sysprep tool. This is a
        Sysprep, LinuxPrep, or SysprepText object.
        '''
        return self.data['identity']

    @property
    def nicSettingMap(self):
        '''IP settings that are specific to a particular virtual network adapter. The
        AdapterMapping object maps a network adapter's MAC address to its Adapter
        settings object. May be empty if there are no network adapters, else
        should match number of network adapters in the VM.
        '''
        return self.data['nicSettingMap']

    @property
    def options(self):
        '''Optional operations (either LinuxOptions or WinOptions).
        '''
        return self.data['options']

