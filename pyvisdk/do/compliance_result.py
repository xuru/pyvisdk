
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ComplianceResult(DynamicData):
    '''DataObject representing the result from a ComplianceCheck
    '''
    
    def __init__(self, checkTime, complianceStatus, entity, failure, profile):
        # MUST define these
        super(ComplianceResult, self).__init__()
    
        self.data['checkTime'] = checkTime
        self.data['complianceStatus'] = complianceStatus
        self.data['entity'] = entity
        self.data['failure'] = failure
        self.data['profile'] = profile
    
    
    @property
    def checkTime(self):
        '''Time at which compliance check was last run on the entity
        '''
        return self.data['checkTime']

    @property
    def complianceStatus(self):
        '''Indicates the compliance status of the entity. See
        '''
        return self.data['complianceStatus']

    @property
    def entity(self):
        '''Entity on which the compliance check was carried out. Entity can be a Cluster,
        Host and so on.
        '''
        return self.data['entity']

    @property
    def failure(self):
        '''If complianceStatus is non-compliant, failure will contain additional information
        about the compliance errors.
        '''
        return self.data['failure']

    @property
    def profile(self):
        '''Profile for which the ComplianceResult applies
        '''
        return self.data['profile']

