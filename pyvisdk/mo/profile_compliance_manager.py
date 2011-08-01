
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
    
    

    def ClearComplianceStatus(self):
        '''Clear the saved ComplianceResult based on profile and entity filtering criteria.
        '''
        
        return self.delegate("ClearComplianceStatus")()
        

    def QueryExpressionMetadata(self):
        '''Query the metadata for the expressions.

        :rtype: ProfileExpressionMetadata[] 

        '''
        
        return self.delegate("QueryExpressionMetadata")()
        

    def QueryComplianceStatus(self):
        '''Query the compliance status based on Profile and Entity filter.

        :rtype: ComplianceResult[] 

        '''
        
        return self.delegate("QueryComplianceStatus")()
        

    def CheckCompliance_Task(self):
        '''Check compliance of an entity against a Profile.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CheckCompliance_Task")()
        
