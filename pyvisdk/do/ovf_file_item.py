
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OvfFileItem(DynamicData):
    '''An FileItem represents a file that must be uploaded by the caller when the
        inventory objects has been created in VI. These objects are created by
        ResourcePool.importVApp.Files can either be new files, in which case the
        "create" flag will be true, or updates to existing files in VI. The latter
        is used to support the OVF parentRef mechanism for Disks.
    '''
    
    def __init__(self, chunkSize, cimType, compressionMethod, create, deviceId, path, size):
        # MUST define these
        super(OvfFileItem, self).__init__()
    
        self.data['chunkSize'] = chunkSize
        self.data['cimType'] = cimType
        self.data['compressionMethod'] = compressionMethod
        self.data['create'] = create
        self.data['deviceId'] = deviceId
        self.data['path'] = path
        self.data['size'] = size
    
    
    @property
    def chunkSize(self):
        '''The chunksize as specified by the OVF specification. If this attribute is set, the
        "path" attribute is a prefix to each chunk of the complete file. For
        example, if chunksize is 2000000000 bytes, the actual files might be:
        myfile.000000000 (2000000000 bytes) myfile.000000001 (2000000000 bytes)
        myfile.000000002 (1500000000 bytes)
        '''
        return self.data['chunkSize']

    @property
    def cimType(self):
        '''The CIM type of the device for which this file provides backing.
        '''
        return self.data['cimType']

    @property
    def compressionMethod(self):
        '''The compression method as specified by the OVF specification (for example "gzip"
        or "bzip2").
        '''
        return self.data['compressionMethod']

    @property
    def create(self):
        '''True if the item is not expected to exist in the infrastructure and should
        therefore be created by the caller (for example using HTTP PUT).
        '''
        return self.data['create']

    @property
    def deviceId(self):
        '''Uniquely identifies the device (disk, CD-ROM etc.) within the entity hierarchy.
        '''
        return self.data['deviceId']

    @property
    def path(self):
        '''The path of the item to upload, relative to the path of the OVF descriptor.
        '''
        return self.data['path']

    @property
    def size(self):
        '''The complete size of the file, if it is specified in the OVF descriptor.
        '''
        return self.data['size']

