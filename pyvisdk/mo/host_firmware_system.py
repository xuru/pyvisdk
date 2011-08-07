
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostFirmwareSystem(BaseEntity):
    '''NOTE: This managed object type and all of its methods are experimental and subject
        to change in future releases.The FirmwareSystem managed object type
        provides access to the firmware of an embedded ESX host. It provides
        operations to backup/restore/reset the configuration of an embedded ESX
        host.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostFirmwareSystem):
        # MUST define these
        super(HostFirmwareSystem, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def BackupFirmwareConfiguration(self, force):
        '''Backup the configuration of the host.A bundle containing the configuration of the
        host is generated. The bundle can be downloaded using a HTTP GET operation
        on the URL returned.

        :param force: Forces application of the configuration even if the bundle is mismatched.

        '''
        
        return self.delegate("BackupFirmwareConfiguration")(force)
        

    def QueryFirmwareConfigUploadURL(self, force):
        '''Return the URL on the host to which the configuration bundle must be uploaded for
        a restore operation.

        :param force: Forces application of the configuration even if the bundle is mismatched.

        '''
        
        return self.delegate("QueryFirmwareConfigUploadURL")(force)
        

    def ResetFirmwareToFactoryDefaults(self, force):
        '''Reset the configuration to factory defaults.This method will reset all
        configuration options, including the "admin" password, to the factory
        defaults. The host will be rebooted immediately. The host needs to be in
        maintenance mode before this operation can be performed.

        :param force: Forces application of the configuration even if the bundle is mismatched.

        '''
        
        return self.delegate("ResetFirmwareToFactoryDefaults")(force)
        

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
        
