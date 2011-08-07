
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LicenseAssignmentManager(BaseEntity):
    '''
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.LicenseAssignmentManager):
        # MUST define these
        super(LicenseAssignmentManager, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def QueryAssignedLicenses(self, entity, licenseKey, entityDisplayName):
        '''Get information about all the licenses associated with an entity

        :param entity: ID of the entity. E.g. HostSystem.

        :param licenseKey: A license.

        :param entityDisplayName: Display name for the entity


        :rtype: LicenseManagerLicenseInfo 

        '''
        
        return self.delegate("QueryAssignedLicenses")(entity,licenseKey,entityDisplayName)
        

    def RemoveAssignedLicense(self, entity, licenseKey, entityDisplayName):
        '''Remove licenses associated with an entity

        :param entity: ID of the entity. E.g. HostSystem.

        :param licenseKey: A license.

        :param entityDisplayName: Display name for the entity


        :rtype: LicenseManagerLicenseInfo 

        '''
        
        return self.delegate("RemoveAssignedLicense")(entity,licenseKey,entityDisplayName)
        

    def UpdateAssignedLicense(self, entity, licenseKey, entityDisplayName):
        '''Update the license associated with an entity

        :param entity: ID of the entity. E.g. HostSystem.

        :param licenseKey: A license.

        :param entityDisplayName: Display name for the entity


        :rtype: LicenseManagerLicenseInfo 

        '''
        
        return self.delegate("UpdateAssignedLicense")(entity,licenseKey,entityDisplayName)
        
