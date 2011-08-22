
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LicenseAssignmentManager(BaseEntity):
    ''''''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.LicenseAssignmentManager):
        super(LicenseAssignmentManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    
    
    
    def QueryAssignedLicenses(self):
        '''Get information about all the licenses associated with an entity
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryAssignedLicenses")()
    
    def RemoveAssignedLicense(self):
        '''Remove licenses associated with an entity
        :rtype: None
        :returns: 
        '''
        return self.delegate("RemoveAssignedLicense")()
    
    def UpdateAssignedLicense(self):
        '''Update the license associated with an entity
        :rtype: 
        :returns: 
        '''
        return self.delegate("UpdateAssignedLicense")()