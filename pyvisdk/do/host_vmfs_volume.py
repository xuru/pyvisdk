
from pyvisdk.do.host_file_system_volume import HostFileSystemVolume
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVmfsVolume(HostFileSystemVolume):
    '''The VMFS file system.
    '''
    
    def __init__(self, blockSizeMb, extent, forceMountedInfo, majorVersion, maxBlocks, uuid, version, vmfsUpgradable):
        # MUST define these
        super(HostVmfsVolume, self).__init__()
    
        self.data['blockSizeMb'] = blockSizeMb
        self.data['extent'] = extent
        self.data['forceMountedInfo'] = forceMountedInfo
        self.data['majorVersion'] = majorVersion
        self.data['maxBlocks'] = maxBlocks
        self.data['uuid'] = uuid
        self.data['version'] = version
        self.data['vmfsUpgradable'] = vmfsUpgradable
    
    
    @property
    def blockSizeMb(self):
        '''Block size of VMFS. Determines maximum file size. The maximum number of blocks is
        typically fixed with each specific version of VMFS. To increase the
        maximum size of a VMFS file, increase the block size.
        '''
        return self.data['blockSizeMb']

    @property
    def extent(self):
        '''The list of partition names that comprise this disk's VMFS extents.
        '''
        return self.data['extent']

    @property
    def forceMountedInfo(self):
        '''Information about 'forceMounted' VmfsVolume. When the system detects a copy of a
        VmfsVolume, it will not be auto-mounted on the host and it will be
        detected as 'UnresolvedVmfsVolume'. If user decides to 'forceMount' the
        VmfsVolume on the host, forceMountedInfo will be populated. It will not be
        set for automounted VMFS volumes.
        '''
        return self.data['forceMountedInfo']

    @property
    def majorVersion(self):
        '''Major version number of VMFS.
        '''
        return self.data['majorVersion']

    @property
    def maxBlocks(self):
        '''Maximum number of blocks. Determines maximum file size along with blockSize. See
        information about the blockSize.
        '''
        return self.data['maxBlocks']

    @property
    def uuid(self):
        '''The universally unique identifier assigned to VMFS.
        '''
        return self.data['uuid']

    @property
    def version(self):
        '''Version string. Contains major and minor version numbers.
        '''
        return self.data['version']

    @property
    def vmfsUpgradable(self):
        '''Can the filesystem be upgraded to a newer version.
        '''
        return self.data['vmfsUpgradable']

