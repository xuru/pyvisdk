
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileComplianceManager(BaseEntity):
    '''Methods
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.ProfileComplianceManager):
        # MUST define these
        super(ProfileComplianceManager, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def CheckCompliance_Task(self, profile, entity):
        '''Check compliance of an entity against a Profile.

        :param profile: If specified, check compliance against the specified profiles. If not specified,
        use the profiles associated with the entities. If both Profiles and
        Entities are specified, Check the compliance of each Entity against each
        of the profile specified. For more information, look at the KMap below. P
        represents if Profile is specified. E represents if Entity is specified.

        :param entity: If specified, the compliance check is done against this entity.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CheckCompliance_Task")(profile,entity)
        

    def ClearComplianceStatus(self, profile, entity):
        '''Clear the saved ComplianceResult based on profile and entity filtering criteria.

        :param profile: If specified, clear the ComplianceResult related to the Profile.

        :param entity: If specified, clear the ComplianceResult related to the entity. If profile and
        entity are not specified, all the ComplianceResults will be cleared.

        '''
        
        return self.delegate("ClearComplianceStatus")(profile,entity)
        

    def QueryComplianceStatus(self, profile, entity):
        '''Query the compliance status based on Profile and Entity filter.

        :param profile: If specified, compliance result for the specified profiles will be returned. This
        acts like a filtering criteria for the ComplianceResults based on
        specified profiles.

        :param entity: If specified, compliance results for these entities will be returned. This acts
        like a filtering criteria for the ComplianceResults based on entities.


        :rtype: ComplianceResult[] 

        '''
        
        return self.delegate("QueryComplianceStatus")(profile,entity)
        

    def QueryExpressionMetadata(self, expressionName):
        '''Query the metadata for the expressions.

        :param expressionName: Names of the Expressions for which metadata is requested. If expressionNames are
        not specified, metadata for all known expressions is returned


        :rtype: ProfileExpressionMetadata[] 

        '''
        
        return self.delegate("QueryExpressionMetadata")(expressionName)
        
