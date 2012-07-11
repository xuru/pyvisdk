
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostFirmwareSystem(BaseEntity):
    '''NOTE: This managed object type and all of its methods are experimental and
    subject to change in future releases.The FirmwareSystem managed object type
    provides access to the firmware of an embedded ESX host. It provides operations
    to backup/restore/reset the configuration of an embedded ESX host.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostFirmwareSystem):
        super(HostFirmwareSystem, self).__init__(core, name=name, ref=ref, type=type)

    

    
    
    def BackupFirmwareConfiguration(self):
        '''Backup the configuration of the host.Backup the configuration of the host.
        
        '''
        return self.delegate("BackupFirmwareConfiguration")()
    
    def QueryFirmwareConfigUploadURL(self):
        '''Return the URL on the host to which the configuration bundle must be uploaded
        for a restore operation.
        
        '''
        return self.delegate("QueryFirmwareConfigUploadURL")()
    
    def ResetFirmwareToFactoryDefaults(self):
        '''Reset the configuration to factory defaults.Reset the configuration to factory
        defaults.
        
        '''
        return self.delegate("ResetFirmwareToFactoryDefaults")()
    
    def RestoreFirmwareConfiguration(self, force):
        '''Restore the configuration of the host to that specified in the bundle.Restore
        the configuration of the host to that specified in the bundle.
        
        :param force: Forces application of the configuration even if the bundle is mismatched.
        
        '''
        return self.delegate("RestoreFirmwareConfiguration")(force)