
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileManager(BaseEntity):
    '''This Class is responsible for managing Profiles.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.ProfileManager):
        # MUST define these
        super(ProfileManager, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def QueryPolicyMetadata(self):
        '''Get the Metadata information for the policyNames. PolicyNames are available with
        the defaultProfile obtained by invoking the method createDefaultProfile.

        :rtype: ProfilePolicyMetadata[] 

        '''
        
        return self.delegate("QueryPolicyMetadata")()
        

    def FindAssociatedProfile(self):
        '''Get the profile(s) to which this entity is associated. The list of profiles will
        only include profiles known to this profileManager.

        :rtype: ManagedObjectReference[] to a Profile[] 

        '''
        
        return self.delegate("FindAssociatedProfile")()
        

    def CreateProfile(self, createSpec):
        '''Create a profile from the specified CreateSpec.

        :param createSpec: Specification for the profile being created. Usually a derived class CreateSpec can be used to create the Profile.


        :rtype: ManagedObjectReference to a Profile 

        '''
        
        return self.delegate("CreateProfile")(createSpec)
        
