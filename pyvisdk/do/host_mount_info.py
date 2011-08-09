
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostMountInfo(DynamicData):
    '''The HostMountInfo data object provides information related to a configured mount
        point. This object does not include information about the mounted file
        system. (See HostFileSystemMountInfo.)
    '''
    
    def __init__(self, accessible, accessMode, path):
        # MUST define these
        super(HostMountInfo, self).__init__()
    
        self.data['accessible'] = accessible
        self.data['accessMode'] = accessMode
        self.data['path'] = path
    
    
    @property
    def accessible(self):
        '''Flag that indicates if the datastore is currently accessible from the host.
        '''
        return self.data['accessible']

    @property
    def accessMode(self):
        '''Access mode to the underlying file system for this host.
        '''
        return self.data['accessMode']

    @property
    def path(self):
        '''Local file path where file system volume is mounted, if applicable. This path
        identifies the file system volume from the point of view of the host.
        '''
        return self.data['path']

