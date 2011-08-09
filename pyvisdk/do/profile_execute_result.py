
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileExecuteResult(DynamicData):
    '''Class describing the result of the Execute operation.
    '''
    
    def __init__(self, configSpec, error, inapplicablePath, requireInput, status):
        # MUST define these
        super(ProfileExecuteResult, self).__init__()
    
        self.data['configSpec'] = configSpec
        self.data['error'] = error
        self.data['inapplicablePath'] = inapplicablePath
        self.data['requireInput'] = requireInput
        self.data['status'] = status
    
    
    @property
    def configSpec(self):
        '''configSpec will be valid only if status == success
        '''
        return self.data['configSpec']

    @property
    def error(self):
        '''List of errors that were encountered during execute. This field will be set if
        status is set to error.
        '''
        return self.data['error']

    @property
    def inapplicablePath(self):
        '''List of paths that are not applicable for this execute. e.g: If the precheck
        policies do not pass on a PortGroup, PortGroup will not be created. The
        user can ignore this subtree. This might be used the UI to not show the
        particular part of the tree.
        '''
        return self.data['inapplicablePath']

    @property
    def requireInput(self):
        '''List of paths that still need user Input. This can be used by the UI to highlight
        the particular fields. In future this could be used to ask the user for
        input in multiple rounds instead of filling up the whole input at once.
        Here is an illustration: In the first pass, the user just fills up bare
        minimum inputs needed. Once that data is sent to the server, the server
        evaluates the Profile and might decide to invalidate a particular part of
        the subtree or enable a new subtree in the profile. Which would result in
        a new set of invalidPaths and requireInput propertyPaths. The caller (UI)
        can keep calling the function in multiple steps till success. If there are
        values that are filled in in the previous iteration, they will be returned
        in requireInput[].param.
        '''
        return self.data['requireInput']

    @property
    def status(self):
        '''Status of the execute operation Will be one of the enumerations in #Status
        '''
        return self.data['status']

