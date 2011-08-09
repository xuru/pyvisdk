
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HttpNfcLeaseManifestEntry(DynamicData):
    '''Provides a manifest for downloaded (exported) files and disks.
    '''
    
    def __init__(self, capacity, disk, key, populatedSize, sha1, size):
        # MUST define these
        super(HttpNfcLeaseManifestEntry, self).__init__()
    
        self.data['capacity'] = capacity
        self.data['disk'] = disk
        self.data['key'] = key
        self.data['populatedSize'] = populatedSize
        self.data['sha1'] = sha1
        self.data['size'] = size
    
    
    @property
    def capacity(self):
        '''The capacity of the disk, if the file is a virtual disk backing.
        '''
        return self.data['capacity']

    @property
    def disk(self):
        '''True if the downloaded file is a virtual disk backing.
        '''
        return self.data['disk']

    @property
    def key(self):
        '''Key used to match this entry with the corresponding DeviceUrl entry in info.
        '''
        return self.data['key']

    @property
    def populatedSize(self):
        '''The populated size of the disk, if the file is a virtual disk backing.
        '''
        return self.data['populatedSize']

    @property
    def sha1(self):
        '''SHA-1 checksum of the data stream sent from the server. This can be used to verify
        that the bytes received by the client match those sent by the HttpNfc
        server.
        '''
        return self.data['sha1']

    @property
    def size(self):
        '''Size of the downloaded file.
        '''
        return self.data['size']

