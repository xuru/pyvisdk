
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DatastoreMountPathDatastorePair(DynamicData):
    '''Contains a mapping of an old mount path and its corresponding resignatured or
        remounted datastore
    '''
    
    def __init__(self, datastore, oldMountPath):
        # MUST define these
        super(DatastoreMountPathDatastorePair, self).__init__()
    
        self.data['datastore'] = datastore
        self.data['oldMountPath'] = oldMountPath
    
    
    @property
    def datastore(self):
        '''The resignatured or remounted datastore corresponding to the oldMountPath
        '''
        return self.data['datastore']

    @property
    def oldMountPath(self):
        '''Old file path where file system volume is mounted, which should be path value in
        HostMountInfo
        '''
        return self.data['oldMountPath']

