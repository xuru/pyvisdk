
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileManager(BaseEntity):
    '''Properties
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.ProfileManager):
        # MUST define these
        super(ProfileManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def profile(self):
        '''A list of profiles known to this ProfileManager.
        '''
        return self.update('profile')


    def CreateProfile(self, createSpec):
        '''Create a profile from the specified CreateSpec.

        :param createSpec: Specification for the profile being created. Usually a derived class CreateSpec
        can be used to create the Profile.


        :rtype: Profile 

        '''
        
        return self.delegate("CreateProfile")(createSpec)
        

    def FindAssociatedProfile(self, entity):
        '''Get the profile(s) to which this entity is associated. The list of profiles will
        only include profiles known to this profileManager.

        :param entity: Entity for which profile is being looked up.


        :rtype: Profile[] 

        '''
        
        return self.delegate("FindAssociatedProfile")(entity)
        

    def QueryPolicyMetadata(self, policyName):
        '''Get the Metadata information for the policyNames. PolicyNames are available with
        the defaultProfile obtained by invoking the method createDefaultProfile.

        :param policyName: Retrieve metadata for the specified policyNames. If policyName is not specified,
        metadata for all policies will be returned.


        :rtype: ProfilePolicyMetadata[] 

        '''
        
        return self.delegate("QueryPolicyMetadata")(policyName)
        
