
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPatchManagerResult(DynamicData):
    '''The result of the operation. Some of the fields are only valid for specific
        operations.
    '''
    
    def __init__(self, status, version, xmlResult):
        # MUST define these
        super(HostPatchManagerResult, self).__init__()
    
        self.data['status'] = status
        self.data['version'] = version
        self.data['xmlResult'] = xmlResult
    
    
    @property
    def status(self):
        '''The scan results for each patch.
        '''
        return self.data['status']

    @property
    def version(self):
        '''The version of the scan result schema.
        '''
        return self.data['version']

    @property
    def xmlResult(self):
        '''The scan results in XML format.
        '''
        return self.data['xmlResult']

