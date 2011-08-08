
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


    def AssociateProfile(self, entity):
        '''Associate a profile with a managed entity.

        :param entity: to a ManagedEntity[]The entity(s) to associate with the profile. If entity is
        already associted with the profile, association is maintained and
        operation is treated as a no-op. throws InvalidType If the entity is of an
        unexpeted type. throws InvalidArgument If the association conflicts with
        existing association.

        '''
        
        return self.delegate("AssociateProfile")(entity)
        

    def CheckProfileCompliance_Task(self, entity):
        '''Check compliance of an entity against a Profile.

        :param entity: to a ManagedEntity[]If specified, the compliance check is done against this
        entity. If the entity is not specified, a compliance check will be run on
        all the entities associated with the profile. Entity need not be
        associated with the profile.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CheckProfileCompliance_Task")(entity)
        

    def DestroyProfile(self):
        '''Destory the Profile
        '''
        
        return self.delegate("DestroyProfile")()
        

    def DissociateProfile(self, entity):
        '''Dissociate a profile from a managed entity.

        :param entity: to a ManagedEntity[]Entity(s) from which to dissociate the profile. If unset, the
        profile is dissociated from all managed entities it is currently
        associated with. If the specified entity is not associated with the
        profile, the operation is a no-op. throws InvalidArgument If the
        dissociation conflicts with existing association.

        '''
        
        return self.delegate("DissociateProfile")(entity)
        

    def ExportProfile(self):
        '''Export the profile into a serialized form. The serialized string can then be used
        to create a profile using SerializedCreateSpec

        :rtype: xsd:string 

        '''
        
        return self.delegate("ExportProfile")()
        
