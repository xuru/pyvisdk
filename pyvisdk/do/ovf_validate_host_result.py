
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OvfValidateHostResult(DynamicData):
    '''
    '''
    
    def __init__(self, downloadSize, error, flatDeploymentSize, sparseDeploymentSize, supportedDiskProvisioning, warning):
        # MUST define these
        super(OvfValidateHostResult, self).__init__()
    
        self.data['downloadSize'] = downloadSize
        self.data['error'] = error
        self.data['flatDeploymentSize'] = flatDeploymentSize
        self.data['sparseDeploymentSize'] = sparseDeploymentSize
        self.data['supportedDiskProvisioning'] = supportedDiskProvisioning
        self.data['warning'] = warning
    
    
    @property
    def downloadSize(self):
        '''The total amount of data that must be transferred to download the entity.
        '''
        return self.data['downloadSize']

    @property
    def error(self):
        '''Errors that happened during validation. The presence of faults in this list
        indicates that the validation failed.
        '''
        return self.data['error']

    @property
    def flatDeploymentSize(self):
        '''The total amount of space required to deploy the entity if using flat disks.
        '''
        return self.data['flatDeploymentSize']

    @property
    def sparseDeploymentSize(self):
        '''The total amount of space required to deploy the entity using sparse disks, if
        known.
        '''
        return self.data['sparseDeploymentSize']

    @property
    def supportedDiskProvisioning(self):
        '''An array of the disk provisioning type supported by the target host system.
        '''
        return self.data['supportedDiskProvisioning']

    @property
    def warning(self):
        '''Non-fatal warnings from the validation.
        '''
        return self.data['warning']

