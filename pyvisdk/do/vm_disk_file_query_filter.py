
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmDiskFileQueryFilter(DynamicData):
    '''The filter for the virtual disk primary file.
    '''
    
    def __init__(self, controllerType, diskType, matchHardwareVersion, thin):
        # MUST define these
        super(VmDiskFileQueryFilter, self).__init__()
    
        self.data['controllerType'] = controllerType
        self.data['diskType'] = diskType
        self.data['matchHardwareVersion'] = matchHardwareVersion
        self.data['thin'] = thin
    
    
    @property
    def controllerType(self):
        '''If this optional property is set, only virtual disk files that have a controller
        type that matches one of the controller types specified are returned. If
        no controller types are specified, this search criteria is ignored.
        '''
        return self.data['controllerType']

    @property
    def diskType(self):
        '''If this optional property is set, only the virtual disk primary files that match
        one of the specified disk types are selected. If no disk types are
        specified, this search criteria is ignored.
        '''
        return self.data['diskType']

    @property
    def matchHardwareVersion(self):
        '''If this optional property is set, only virtual disk primary files that match one
        of the specified hardware versions are selected. If no versions are
        specified, this search criteria is ignored.
        '''
        return self.data['matchHardwareVersion']

    @property
    def thin(self):
        '''This optional property can be used to filter disks based on whether they are thin-
        provsioned or not: if set to true, only thin-provisioned disks are
        returned, and vice-versa.
        '''
        return self.data['thin']

