
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class Profile(BaseEntity):
    '''
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.Profile):
        # MUST define these
        super(Profile, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def complianceStatus(self):
        '''Overall compliance of entities associated with this profile. If one of the
        entities is out of compliance, profile is out of compliance. If all
        entities are in compliance, profile is in compliance. If compliance status
        of one of the entities is unknown, compliance status of the profile is
        unknown. See
        '''
        return self.update('complianceStatus')

    @property
    def config(self):
        '''Configuration of the profile
        '''
        return self.update('config')

    @property
    def createdTime(self):
        '''Time at which the profile was created
        '''
        return self.update('createdTime')

    @property
    def description(self):
        '''Localizeable Description of the Profile
        '''
        return self.update('description')

    @property
    def entity(self):
        '''List of ManagedEntities associated with the Profile
        '''
        return self.update('entity')

    @property
    def modifiedTime(self):
        '''Time at which the profile was last modified
        '''
        return self.update('modifiedTime')


    def AssociateProfile(self):
        '''Associate a profile with a managed entity.

        :rtype: xsd:string 

        '''
        
        return self.delegate("AssociateProfile")()
        

    def CheckProfileCompliance_Task(self):
        '''Check compliance of an entity against a Profile.

        :rtype: xsd:string 

        '''
        
        return self.delegate("CheckProfileCompliance_Task")()
        

    def DestroyProfile(self):
        '''Destory the Profile

        :rtype: xsd:string 

        '''
        
        return self.delegate("DestroyProfile")()
        

    def DissociateProfile(self):
        '''Dissociate a profile from a managed entity.

        :rtype: xsd:string 

        '''
        
        return self.delegate("DissociateProfile")()
        

    def ExportProfile(self):
        '''Export the profile into a serialized form. The serialized string can then be used
        to create a profile using SerializedCreateSpec

        :rtype: xsd:string 

        '''
        
        return self.delegate("ExportProfile")()
        
