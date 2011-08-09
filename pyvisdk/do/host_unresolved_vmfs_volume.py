
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostUnresolvedVmfsVolume(DynamicData):
    '''Information about detected unbound, unresolved VMFS volume. An unresolved VMFS
        volume is reported when one or more device partitions of volume are
        detected to have copies of extents of the volume. Such copies can be
        created via replication or snapshots.UnresolvedVmfsVolume are not mounted
        on the host where they are detected. User may choose to resignature the
        volume in which case a new Uuid is assigned to the volume and contents of
        the VMFS volume is kept intact.User may choose to keep the original Uuid
        and mount the VMFS volume as it is on the given host. In this case, user
        has choosen to mount the copy of the VMFS volume on that host with no
        change to the original Uuid. This may fail with VmfsVolumeAlreadyMounted
        exception if there is an existing VMFS volume with the same Uuid mounted
        somewhere in the same datacenter.Simple diagram representing the possible
        operations on UnresolvedVmfsVolumeSee HostStorageSystem
    '''
    
    def __init__(self, extent, resolveStatus, totalBlocks, vmfsLabel, vmfsUuid):
        # MUST define these
        super(HostUnresolvedVmfsVolume, self).__init__()
    
        self.data['extent'] = extent
        self.data['resolveStatus'] = resolveStatus
        self.data['totalBlocks'] = totalBlocks
        self.data['vmfsLabel'] = vmfsLabel
        self.data['vmfsUuid'] = vmfsUuid
    
    
    @property
    def extent(self):
        '''List of detected copies of VMFS extents.
        '''
        return self.data['extent']

    @property
    def resolveStatus(self):
        '''Information related to how the volume might be resolved.
        '''
        return self.data['resolveStatus']

    @property
    def totalBlocks(self):
        '''Total number of blocks in this volume.
        '''
        return self.data['totalBlocks']

    @property
    def vmfsLabel(self):
        '''The detected VMFS label name
        '''
        return self.data['vmfsLabel']

    @property
    def vmfsUuid(self):
        '''The detected VMFS UUID
        '''
        return self.data['vmfsUuid']

