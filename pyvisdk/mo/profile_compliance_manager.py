
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileComplianceManager(BaseEntity):
    '''Interface handling the Compliance aspects of entities.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.ProfileComplianceManager):
        super(ProfileComplianceManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    
    
    
    def CheckCompliance_Task(self):
        '''Check compliance of an entity against a Profile.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("CheckCompliance_Task")()
    
    def ClearComplianceStatus(self):
        '''Clear the saved ComplianceResult based on profile and entity filtering
        criteria.
        :rtype: None
        :returns: 
        '''
        return self.delegate("ClearComplianceStatus")()
    
    def QueryComplianceStatus(self):
        '''Query the compliance status based on Profile and Entity filter.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryComplianceStatus")()
    
    def QueryExpressionMetadata(self):
        '''Query the metadata for the expressions.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryExpressionMetadata")()