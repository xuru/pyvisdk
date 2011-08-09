
from pyvisdk.do.virtual_device_file_backing_info import VirtualDeviceFileBackingInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDiskFlatVer2BackingInfo(VirtualDeviceFileBackingInfo):
    '''This data object type contains information about backing a virtual disk using a
        virtual disk file on the host, in the flat file format used by VMware
        Server, ESX Server 2.x, and ESX Server 3.x. Flat disks are allocated when
        created, unlike sparse disks, which grow as needed.
    '''
    
    def __init__(self, changeId, contentId, diskMode, eagerlyScrub, parent, split, thinProvisioned, uuid, writeThrough):
        # MUST define these
        super(VirtualDiskFlatVer2BackingInfo, self).__init__()
    
        self.data['changeId'] = changeId
        self.data['contentId'] = contentId
        self.data['diskMode'] = diskMode
        self.data['eagerlyScrub'] = eagerlyScrub
        self.data['parent'] = parent
        self.data['split'] = split
        self.data['thinProvisioned'] = thinProvisioned
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
        * independent_nonpersistent * nonpersistent * undoable * append
        '''
        return self.data['diskMode']

    @property
    def eagerlyScrub(self):
        '''Flag to indicate to the underlying filesystem whether the virtual disk backing
        file should be scrubbed completely at this time.
        '''
        return self.data['eagerlyScrub']

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
    def thinProvisioned(self):
        '''Flag to indicate to the underlying filesystem, whether the virtual disk backing
        file should be allocated lazily (using thin provisioning). This flag is
        only used for file systems that support configuring the provisioning
        policy on a per file basis, such as VMFS3.
        '''
        return self.data['thinProvisioned']

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

