
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostMultipathInfoLogicalUnit(DynamicData):
    '''This data object type represents a storage entity that provides disk blocks to a
        host.
    '''
    
    def __init__(self, id, key, lun, path, policy, storageArrayTypePolicy):
        # MUST define these
        super(HostMultipathInfoLogicalUnit, self).__init__()
    
        self.data['id'] = id
        self.data['key'] = key
        self.data['lun'] = lun
        self.data['path'] = path
        self.data['policy'] = policy
        self.data['storageArrayTypePolicy'] = storageArrayTypePolicy
    
    
    @property
    def id(self):
        '''Identifier of LogicalUnit.
        '''
        return self.data['id']

    @property
    def key(self):
        '''Linkable identifier.
        '''
        return self.data['key']

    @property
    def lun(self):
        '''The SCSI device corresponding to logical unit.
        '''
        return self.data['lun']

    @property
    def path(self):
        '''The array of paths available to access this LogicalUnit.
        '''
        return self.data['path']

    @property
    def policy(self):
        '''Policy that the logical unit should use when selecting a path.
        '''
        return self.data['policy']

    @property
    def storageArrayTypePolicy(self):
        '''Policy used to determine how a storage device is accessed. This policy is
        currently immutable.
        '''
        return self.data['storageArrayTypePolicy']

