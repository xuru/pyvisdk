
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostFileSystemVolume(DynamicData):
    '''Detailed information about a file system. This is a base type for derived types
        that have more specific details about specific filesystem types.Typically
        a FileSystem is exposed as a datatore See DatastoreInfo See HostVmfsVolume
        See HostNasVolume See HostLocalFileSystemVolume
    '''
    
    def __init__(self, capacity, name, type):
        # MUST define these
        super(HostFileSystemVolume, self).__init__()
    
        self.data['capacity'] = capacity
        self.data['name'] = name
        self.data['type'] = type
    
    
    @property
    def capacity(self):
        '''The capacity of the file system volume, in bytes.
        '''
        return self.data['capacity']

    @property
    def name(self):
        '''Name of the file system volume.
        '''
        return self.data['name']

    @property
    def type(self):
        '''Type of file system volume.
        '''
        return self.data['type']

