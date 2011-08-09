
from pyvisdk.do.virtual_device_file_backing_info import VirtualDeviceFileBackingInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDiskFlatVer1BackingInfo(VirtualDeviceFileBackingInfo):
    '''This data object type contains information about backing a virtual disk by using a
        virtual disk file on the host, in the flat file format used by GSX Server
        2.x.Flat disks are allocated when created, unlike sparse disks, which grow
        as needed.
    '''
    
    def __init__(self, contentId, diskMode, parent, split, writeThrough):
        # MUST define these
        super(VirtualDiskFlatVer1BackingInfo, self).__init__()
    
        self.data['contentId'] = contentId
        self.data['diskMode'] = diskMode
        self.data['parent'] = parent
        self.data['split'] = split
        self.data['writeThrough'] = writeThrough
    
    
    @property
    def contentId(self):
        '''Content ID of the virtual disk file, if available.
        '''
        return self.data['contentId']

    @property
    def diskMode(self):
        '''The disk persistence mode. Valid modes are: * persistent * nonpersistent *
        undoable
        '''
        return self.data['diskMode']

    @property
    def parent(self):
        '''The parent of this virtual disk file, if this is a delta disk backing. This will
        be unset if this is not a delta disk backing.
        '''
        return self.data['parent']

    @property
    def split(self):
        '''Flag to indicate the type of virtual disk file: split or monolithic. If true, the
        virtual disk is stored in multiple files, each 2GB.
        '''
        return self.data['split']

    @property
    def writeThrough(self):
        '''Flag to indicate whether writes should go directly to the file system or should be
        buffered.
        '''
        return self.data['writeThrough']

