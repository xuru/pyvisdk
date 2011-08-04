
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostFirmwareSystem(BaseEntity):
    '''Properties
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostFirmwareSystem):
        # MUST define these
        super(HostFirmwareSystem, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def BackupFirmwareConfiguration(self):
        '''Backup the configuration of the host.A bundle containing the configuration of the
        host is generated. The bundle can be downloaded using a HTTP GET operation
        on the URL returned.

        :rtype: xsd:string 

        '''
        
        return self.delegate("BackupFirmwareConfiguration")()
        

    def QueryFirmwareConfigUploadURL(self):
        '''Return the URL on the host to which the configuration bundle must be uploaded for
        a restore operation.

        :rtype: xsd:string 

        '''
        
        return self.delegate("QueryFirmwareConfigUploadURL")()
        

    def ResetFirmwareToFactoryDefaults(self):
        '''Reset the configuration to factory defaults.This method will reset all
        configuration options, including the "admin" password, to the factory
        defaults. The host will be rebooted immediately. The host needs to be in
        maintenance mode before this operation can be performed.
        '''
        
        return self.delegate("ResetFirmwareToFactoryDefaults")()
        

    def RestoreFirmwareConfiguration(self, force):
        '''Restore the configuration of the host to that specified in the bundle.The bundle
        is expected to be uploaded to the URL retrieved via queryConfigUploadURL.
        This method will reset all configuration options, including the "admin"
        password, to the values in the bundle. The host will be rebooted
        immediately. The host needs to be in maintenance mode before this
        operation can be performed.

        :param force: Forces application of the configuration even if the bundle is mismatched.

        '''
        
        return self.delegate("RestoreFirmwareConfiguration")(force)
        
