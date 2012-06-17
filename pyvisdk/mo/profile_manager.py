
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileManager(BaseEntity):
    '''This Class is responsible for managing Profiles.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.ProfileManager):
        super(ProfileManager, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def profile(self):
        '''A list of profiles known to this ProfileManager.'''
        return self.update('profile')

    
    
    def CreateProfile(self, createSpec):
        '''Create a profile from the specified CreateSpec.
        
        :param createSpec: Specification for the profile being created. Usually a derived class CreateSpec can be used to create the Profile.
        
        '''
        return self.delegate("CreateProfile")(createSpec)
    
    def FindAssociatedProfile(self, entity):
        '''Get the profile(s) to which this entity is associated. The list of profiles
        will only include profiles known to this profileManager.
        
        :param entity: Entity for which profile is being looked up.
        
        '''
        return self.delegate("FindAssociatedProfile")(entity)
    
    def QueryPolicyMetadata(self, policyName=None, profile=None):
        '''Get the Metadata information for the policyNames. PolicyNames are available
        with the defaultProfile obtained by invoking the method createDefaultProfile.
        
        :param policyName: Retrieve metadata for the specified policyNames. If policyName is not specified, metadata for all policies will be returned.
        
        :param profile: Base profile whose context needs to be used during the operationvSphere API 5.0
        
        '''
        return self.delegate("QueryPolicyMetadata")(policyName, profile)