
from pyvisdk.do.virtual_device_file_backing_info import VirtualDeviceFileBackingInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDiskRawDiskMappingVer1BackingInfo(VirtualDeviceFileBackingInfo):
    '''This data object type contains information about backing a virtual disk using a
        raw device mapping. Supported for ESX Server 2.5 and 3.x.
    '''
    
    def __init__(self, changeId, compatibilityMode, contentId, deviceName, diskMode, lunUuid, parent, uuid):
        # MUST define these
        super(VirtualDiskRawDiskMappingVer1BackingInfo, self).__init__()
    
        self.data['changeId'] = changeId
        self.data['compatibilityMode'] = compatibilityMode
        self.data['contentId'] = contentId
        self.data['deviceName'] = deviceName
        self.data['diskMode'] = diskMode
        self.data['lunUuid'] = lunUuid
        self.data['parent'] = parent
        self.data['uuid'] = uuid
    
    
    @property
    def changeId(self):
        '''The change ID of the virtual disk for the corresponding snapshot or virtual
        machine. This can be used to track incremental changes to a virtual disk.
        See QueryChangedDiskAreas.
        '''
        return self.data['changeId']

    @property
    def compatibilityMode(self):
        '''The compatibility mode of the raw disk mapping (RDM). This must be specified when
        a new virtual disk with an RDM backing is created. On subsequent virtual
        machine reconfigurations, this property should be handled as follows,
        depending on the version of the host:
        '''
        return self.data['compatibilityMode']

    @property
    def contentId(self):
        '''Content ID of the virtual disk file, if available.
        '''
        return self.data['contentId']

    @property
    def deviceName(self):
        '''The host-specific device the LUN is being accessed through. If the target LUN is
        not available on the host then it is empty. For example, this could happen
        if it has accidentally been masked out.
        '''
        return self.data['deviceName']

    @property
    def diskMode(self):
        '''The disk mode. Valid values are: * persistent * independent_persistent *
        independent_nonpersistent * nonpersistent * undoable * append
        '''
        return self.data['diskMode']

    @property
    def lunUuid(self):
        '''Unique identifier of the LUN accessed by the raw disk mapping.
        '''
        return self.data['lunUuid']

    @property
    def parent(self):
        '''The parent of this virtual disk file, if this is a delta disk backing. This will
        be unset if this is not a delta disk backing.
        '''
        return self.data['parent']

    @property
    def uuid(self):
        '''Disk UUID for the virtual disk, if available. Disk UUID is not available if the
        raw disk mapping is in physical compatibility mode.
        '''
        return self.data['uuid']

