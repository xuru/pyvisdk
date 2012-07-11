
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class Profile(BaseEntity):
    '''The managed object is the base class for host and cluster profiles.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.Profile):
        super(Profile, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def complianceStatus(self):
        '''Overall compliance of entities associated with this profile. If one of the
        entities is out of compliance, the profile is'''
        return self.update('complianceStatus')
    @property
    def config(self):
        '''Configuration data for the profile.'''
        return self.update('config')
    @property
    def createdTime(self):
        '''Time at which the profile was created.'''
        return self.update('createdTime')
    @property
    def description(self):
        '''Localizable description of the profile'''
        return self.update('description')
    @property
    def entity(self):
        '''List of managed entities associated with the profile.'''
        return self.update('entity')
    @property
    def modifiedTime(self):
        '''Time at which the profile was last modified.'''
        return self.update('modifiedTime')
    @property
    def name(self):
        '''Name of the profile.'''
        return self.update('name')

    
    
    def AssociateProfile(self, entity):
        '''Associate a profile with a managed entity. You can check the compliance of
        entities associated with a profile by calling the CheckProfileCompliance_Task
        method.
        
        :param entity: The entity(s) to associate with the profile. If an entity is already associated with the profile, the association is maintained and the vCenter Server does not perform any action.
        
        '''
        return self.delegate("AssociateProfile")(entity)
    
    def CheckProfileCompliance_Task(self, entity=None):
        '''Check compliance of an entity against a Profile.
        
        :param entity: If specified, the compliance check is performed on this entity. If the entity is not specified, the vCenter Server runs a compliance check on all the entities associated with the profile. The entity does not have to be associated with the profile.
        
        '''
        return self.delegate("CheckProfileCompliance_Task")(entity)
    
    def DestroyProfile(self):
        '''Destroy the profile.
        
        '''
        return self.delegate("DestroyProfile")()
    
    def DissociateProfile(self, entity=None):
        '''Remove the association between a profile and a managed entity.
        
        :param entity: List of entities. The vCenter Server will remove the associations that the profile has with the entities in the list. If unset, the Server removes all the associations that the profile has with any managed entities in the inventory. If the specified entity is not associated with the profile, the Server does not perform any action.
        
        '''
        return self.delegate("DissociateProfile")(entity)
    
    def ExportProfile(self):
        '''Export the profile in a serialized form. To use the serialized string to create
        a profile, specify a ProfileSerializedCreateSpec when you call the
        HostProfileManager.CreateProfile method.
        
        '''
        return self.delegate("ExportProfile")()
    
    def RetrieveDescription(self):
        '''Returns the localizable description for the profile.
        
        '''
        return self.delegate("RetrieveDescription")()