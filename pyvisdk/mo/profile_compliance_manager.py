
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileComplianceManager(BaseEntity):
    '''Interface handling the Compliance aspects of entities.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.ProfileComplianceManager):
        # MUST define these
        super(ProfileComplianceManager, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def CheckCompliance_Task(self, expressionName):
        '''Check compliance of an entity against a Profile.

        :param expressionName: Names of the Expressions for which metadata is requested. If expressionNames are
        not specified, metadata for all known expressions is returned


        :rtype: ProfileExpressionMetadata[] 

        '''
        
        return self.delegate("CheckCompliance_Task")(expressionName)
        

    def ClearComplianceStatus(self, expressionName):
        '''Clear the saved ComplianceResult based on profile and entity filtering criteria.

        :param expressionName: Names of the Expressions for which metadata is requested. If expressionNames are
        not specified, metadata for all known expressions is returned


        :rtype: ProfileExpressionMetadata[] 

        '''
        
        return self.delegate("ClearComplianceStatus")(expressionName)
        

    def QueryComplianceStatus(self, expressionName):
        '''Query the compliance status based on Profile and Entity filter.

        :param expressionName: Names of the Expressions for which metadata is requested. If expressionNames are
        not specified, metadata for all known expressions is returned


        :rtype: ProfileExpressionMetadata[] 

        '''
        
        return self.delegate("QueryComplianceStatus")(expressionName)
        

    def QueryExpressionMetadata(self, expressionName):
        '''Query the metadata for the expressions.

        :param expressionName: Names of the Expressions for which metadata is requested. If expressionNames are
        not specified, metadata for all known expressions is returned


        :rtype: ProfileExpressionMetadata[] 

        '''
        
        return self.delegate("QueryExpressionMetadata")(expressionName)
        
