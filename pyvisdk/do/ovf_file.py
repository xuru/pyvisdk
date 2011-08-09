
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OvfFile(DynamicData):
    '''Represents a file that the caller has downloaded and stored somewhere
        appropriate.An instance of this class is used to tell OvfManager about the
        choices the caller made about a file. This information is needed when the
        OVF descriptor is generated with createDescriptor.
    '''
    
    def __init__(self, capacity, chunkSize, compressionMethod, deviceId, path, populatedSize, size):
        # MUST define these
        super(OvfFile, self).__init__()
    
        self.data['capacity'] = capacity
        self.data['chunkSize'] = chunkSize
        self.data['compressionMethod'] = compressionMethod
        self.data['deviceId'] = deviceId
        self.data['path'] = path
        self.data['populatedSize'] = populatedSize
        self.data['size'] = size
    
    
    @property
    def capacity(self):
        '''The capacity of the disk backed by this file. This should only be set if the
        device backed by this file is a disk. This value will be written in the
        "capacity" attribute of the corresponding "Disk" element in the OVF
        descriptor.
        '''
        return self.data['capacity']

    @property
    def chunkSize(self):
        '''The chunksize chosen by the caller.
        '''
        return self.data['chunkSize']

    @property
    def compressionMethod(self):
        '''The compression method the caller chose to employ for this file.
        '''
        return self.data['compressionMethod']

    @property
    def deviceId(self):
        '''The ID of the device backed by this file. This ID uniquely identifies the device
        within the entity hierarchy.
        '''
        return self.data['deviceId']

    @property
    def path(self):
        '''The path chosen by the caller for this file. This path becomes the value of the
        "href" attribute of the corresponding "File" element in the OVF
        descriptor.
        '''
        return self.data['path']

    @property
    def populatedSize(self):
        '''The populated size of the disk backed by this file. This should only be set if the
        device backed by this file is a disk. This value will be written in the
        "populatedSize" attribute of the corresponding "Disk" element in the OVF
        descriptor.
        '''
        return self.data['populatedSize']

    @property
    def size(self):
        '''The file size, as observed by the caller during download.
        '''
        return self.data['size']

