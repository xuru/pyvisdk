
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVmfsSpec(DynamicData):
    '''This data object type describes the VMware File System (VMFS) creation
        specification. Once created, these properties for the most part cannot be
        changed. There are a few exceptions.
    '''
    
    def __init__(self, blockSizeMb, extent, majorVersion, volumeName):
        # MUST define these
        super(HostVmfsSpec, self).__init__()
    
        self.data['blockSizeMb'] = blockSizeMb
        self.data['extent'] = extent
        self.data['majorVersion'] = majorVersion
        self.data['volumeName'] = volumeName
    
    
    @property
    def blockSizeMb(self):
        '''The block size of VMFS in megabytes (MB). Determines the maximum file size. If
        this optional property is not set, the maximum file size defaults to the
        maximum file size for the platform.
        '''
        return self.data['blockSizeMb']

    @property
    def extent(self):
        '''Head extent of VMFS. The head extent identifies the VMFS. However, the head extent
        should not be used to identify the VMFS across host reboots. The actual
        identifier is specified in "vmhbaI:T:L" format which is not guaranteed to
        be stable across reboots. Define a volume name that is unique to the host
        and use it to refer to the VMFS. Alternatively, the immutable UUID of the
        VMFS can be used after it is created.
        '''
        return self.data['extent']

    @property
    def majorVersion(self):
        '''Major version number of VMFS. This can be changed if the VMFS is upgraded, but
        this is an irreversible change.
        '''
        return self.data['majorVersion']

    @property
    def volumeName(self):
        '''Volume name of VMFS.
        '''
        return self.data['volumeName']

