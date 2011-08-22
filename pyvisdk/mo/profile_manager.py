
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.base_entity import BaseEntity
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
    
    
    
    def CreateProfile(self):
        '''Create a profile from the specified CreateSpec.
        :rtype: ManagedObjectReference to a Profile
        :returns: 
        '''
        return self.delegate("CreateProfile")()
    
    def FindAssociatedProfile(self):
        '''Get the profile(s) to which this entity is associated. The list of profiles
        will only include profiles known to this profileManager.
        :rtype: ManagedObjectReference[] to a Profile[]
        :returns: 
        '''
        return self.delegate("FindAssociatedProfile")()
    
    def QueryPolicyMetadata(self):
        '''Get the Metadata information for the policyNames. PolicyNames are available
        with the defaultProfile obtained by invoking the method createDefaultProfile.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryPolicyMetadata")()