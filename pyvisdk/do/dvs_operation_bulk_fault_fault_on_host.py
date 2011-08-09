
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DvsOperationBulkFaultFaultOnHost(DynamicData):
    '''The fault occured on the host during an operation.
    '''
    
    def __init__(self, fault, host):
        # MUST define these
        super(DvsOperationBulkFaultFaultOnHost, self).__init__()
    
        self.data['fault'] = fault
        self.data['host'] = host
    
    
    @property
    def fault(self):
        '''The fault that occured.
        '''
        return self.data['fault']

    @property
    def host(self):
        '''
        '''
        return self.data['host']

