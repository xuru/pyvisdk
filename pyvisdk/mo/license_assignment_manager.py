
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LicenseAssignmentManager(BaseEntity):
    ''''''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.LicenseAssignmentManager):
        super(LicenseAssignmentManager, self).__init__(core, name=name, ref=ref, type=type)

    

    
    
    def QueryAssignedLicenses(self, entityId=None):
        '''Get information about all the licenses associated with an entity
        
        :param entityId: ID of the entity. E.g. HostSystem.
        
        '''
        return self.delegate("QueryAssignedLicenses")(entityId)
    
    def RemoveAssignedLicense(self, entityId):
        '''Remove licenses associated with an entity
        
        :param entityId: ID of the entity. E.g. HostSystem.
        
        '''
        return self.delegate("RemoveAssignedLicense")(entityId)
    
    def UpdateAssignedLicense(self, entity, licenseKey, entityDisplayName=None):
        '''Update the license associated with an entity
        
        :param entity: ID of the entity. E.g. HostSystem.
        
        :param licenseKey: A license.
        
        :param entityDisplayName: Display name for the entity
        
        '''
        return self.delegate("UpdateAssignedLicense")(entity, licenseKey, entityDisplayName)