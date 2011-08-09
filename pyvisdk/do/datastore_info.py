
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DatastoreInfo(DynamicData):
    '''Detailed information about a datastore. This is a base type for derived types that
        have more specific details about a datastore. See HostVmfsVolume See
        HostNasVolume See HostLocalFileSystemVolume
    '''
    
    def __init__(self, freeSpace, maxFileSize, name, timestamp, url):
        # MUST define these
        super(DatastoreInfo, self).__init__()
    
        self.data['freeSpace'] = freeSpace
        self.data['maxFileSize'] = maxFileSize
        self.data['name'] = name
        self.data['timestamp'] = timestamp
        self.data['url'] = url
    
    
    @property
    def freeSpace(self):
        '''Free space of this datastore, in bytes. The server periodically updates this
        value. It can be explicitly refreshed with the Refresh operation.
        '''
        return self.data['freeSpace']

    @property
    def maxFileSize(self):
        '''The maximum size of a file that can reside on this file system volume.
        '''
        return self.data['maxFileSize']

    @property
    def name(self):
        '''The name of the datastore.
        '''
        return self.data['name']

    @property
    def timestamp(self):
        '''Time when the free-space and capacity values in DatastoreInfo and DatastoreSummary
        were updated.
        '''
        return self.data['timestamp']

    @property
    def url(self):
        '''The unique locator for the datastore.
        '''
        return self.data['url']

