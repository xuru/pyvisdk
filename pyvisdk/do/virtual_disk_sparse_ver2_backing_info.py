
from pyvisdk.do.virtual_device_file_backing_info import VirtualDeviceFileBackingInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDiskSparseVer2BackingInfo(VirtualDeviceFileBackingInfo):
    '''This data object type contains information about backing a virtual disk by using a
        virtual disk file on the host, in the sparse disk format used by VMware
        Server.
    '''
    
    def __init__(self, changeId, contentId, diskMode, parent, spaceUsedInKB, split, uuid, writeThrough):
        # MUST define these
        super(VirtualDiskSparseVer2BackingInfo, self).__init__()
    
        self.data['changeId'] = changeId
        self.data['contentId'] = contentId
        self.data['diskMode'] = diskMode
        self.data['parent'] = parent
        self.data['spaceUsedInKB'] = spaceUsedInKB
        self.data['split'] = split
        self.data['uuid'] = uuid
        self.data['writeThrough'] = writeThrough
    
    
    @property
    def changeId(self):
        '''The change ID of the virtual disk for the corresponding snapshot or virtual
        machine. This can be used to track incremental changes to a virtual disk.
        See QueryChangedDiskAreas.
        '''
        return self.data['changeId']

    @property
    def contentId(self):
        '''Content ID of the virtual disk file, if available.
        '''
        return self.data['contentId']

    @property
    def diskMode(self):
        '''The disk persistence mode. Valid modes are: * persistent * independent_persistent
        * independent_nonpersistent
        '''
        return self.data['diskMode']

    @property
    def parent(self):
        '''The parent of this virtual disk file, if this is a delta disk backing. This will
        be unset if this is not a delta disk backing.
        '''
        return self.data['parent']

    @property
    def spaceUsedInKB(self):
        '''The space in use for this sparse disk. This information is provided when
        retrieving configuration information for an exisiting virtual machine. The
        client cannot modify this information using reconfigure on a virtual
        machine.
        '''
        return self.data['spaceUsedInKB']

    @property
    def split(self):
        '''Flag to indicate the type of virtual disk file: split or monolithic. If true, the
        virtual disk is stored in multiple files, each 2GB.
        '''
        return self.data['split']

    @property
    def uuid(self):
        '''Disk UUID for the virtual disk, if available.
        '''
        return self.data['uuid']

    @property
    def writeThrough(self):
        '''Flag to indicate whether writes should go directly to the file system or should be
        buffered.
        '''
        return self.data['writeThrough']

