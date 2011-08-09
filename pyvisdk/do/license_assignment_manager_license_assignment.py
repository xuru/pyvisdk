
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LicenseAssignmentManagerLicenseAssignment(DynamicData):
    '''
    '''
    
    def __init__(self, assignedLicense, entityDisplayName, entityId, properties, scope):
        # MUST define these
        super(LicenseAssignmentManagerLicenseAssignment, self).__init__()
    
        self.data['assignedLicense'] = assignedLicense
        self.data['entityDisplayName'] = entityDisplayName
        self.data['entityId'] = entityId
        self.data['properties'] = properties
        self.data['scope'] = scope
    
    
    @property
    def assignedLicense(self):
        '''License assigned to the entity
        '''
        return self.data['assignedLicense']

    @property
    def entityDisplayName(self):
        '''Display name of the entity
        '''
        return self.data['entityDisplayName']

    @property
    def entityId(self):
        '''Id for the entity
        '''
        return self.data['entityId']

    @property
    def properties(self):
        '''Additional properties associated with this assignment Some of the properties are:
        "inUseFeatures" -- Features in the license key that are being used by the
        entity "ProductName" -- Name of the entity. Should match the product name
        of the assigned license. "ProductVersion" -- Version of the entity. Should
        match the product version of the assigned license. "Evaluation" --
        EvaluationInfo object representing the evaluation left for the entity.
        '''
        return self.data['properties']

    @property
    def scope(self):
        '''Scope of the entityId
        '''
        return self.data['scope']

