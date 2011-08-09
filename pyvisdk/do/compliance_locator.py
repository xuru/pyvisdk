
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ComplianceLocator(DynamicData):
    '''This dataObject contains information about location of applyProfile which was
        responsible for generation of a particular ComplianceExpression.
    '''
    
    def __init__(self, applyPath, expressionName):
        # MUST define these
        super(ComplianceLocator, self).__init__()
    
        self.data['applyPath'] = applyPath
        self.data['expressionName'] = expressionName
    
    
    @property
    def applyPath(self):
        '''Complete path to the profile/policy which was responsible for the generation of
        the ComplianceExpression. [ProfilePath + policyId] will uniquely identify
        a Policy.
        '''
        return self.data['applyPath']

    @property
    def expressionName(self):
        '''Exression for which the Locator corresponds to
        '''
        return self.data['expressionName']

