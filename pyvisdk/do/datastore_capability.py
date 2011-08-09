
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DatastoreCapability(DynamicData):
    '''Information about the capabilities of this datastore.
    '''
    
    def __init__(self, directoryHierarchySupported, perFileThinProvisioningSupported, rawDiskMappingsSupported, storageIORMSupported):
        # MUST define these
        super(DatastoreCapability, self).__init__()
    
        self.data['directoryHierarchySupported'] = directoryHierarchySupported
        self.data['perFileThinProvisioningSupported'] = perFileThinProvisioningSupported
        self.data['rawDiskMappingsSupported'] = rawDiskMappingsSupported
        self.data['storageIORMSupported'] = storageIORMSupported
    
    
    @property
    def directoryHierarchySupported(self):
        '''Indicates whether or not directories can be created on this datastore.
        '''
        return self.data['directoryHierarchySupported']

    @property
    def perFileThinProvisioningSupported(self):
        '''Indicates whether or not the datastore supports thin provisioning on a per file
        basis. When thin provisioning is used, backing storage is lazily
        allocated.
        '''
        return self.data['perFileThinProvisioningSupported']

    @property
    def rawDiskMappingsSupported(self):
        '''Indicates whether or not raw disk mappings can be created on this datastore.
        '''
        return self.data['rawDiskMappingsSupported']

    @property
    def storageIORMSupported(self):
        '''Indicates whether the datastore supports Storage I/O Resource Management.
        '''
        return self.data['storageIORMSupported']

