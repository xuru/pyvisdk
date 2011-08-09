
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfilePolicyOptionMetadata(DynamicData):
    '''This data object represents the metadata information of a PolicyOption
    '''
    
    def __init__(self, id, parameter):
        # MUST define these
        super(ProfilePolicyOptionMetadata, self).__init__()
    
        self.data['id'] = id
        self.data['parameter'] = parameter
    
    
    @property
    def id(self):
        '''The id of the PolicyOption id.key Identifies the PolicyOption type. id.label
        contains a brief localizable message describing the PolicyOption.
        id.summary contains a localizable summary of the PolicyOption. Summary
        information can contain embedded variable names which can be replaced with
        values from #parameter.
        '''
        return self.data['id']

    @property
    def parameter(self):
        '''Metadata about the parameters of the PolicyOption. The parameter can be a derived
        class of PolicyOptionParameterMetadata too.
        '''
        return self.data['parameter']

