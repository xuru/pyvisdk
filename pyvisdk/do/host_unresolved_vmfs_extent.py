
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostUnresolvedVmfsExtent(DynamicData):
    '''Information about an unresolved VMFS volume extent An unresolved VMFS volume
        extent is a device partition which is detected to have copy of an extent
        of a VMFS volume. Such a copy can be created via replication or snapshots,
        for example. See HostUnresolvedVmfsVolume
    '''
    
    def __init__(self, device, devicePath, endBlock, isHeadExtent, ordinal, reason, startBlock, vmfsUuid):
        # MUST define these
        super(HostUnresolvedVmfsExtent, self).__init__()
    
        self.data['device'] = device
        self.data['devicePath'] = devicePath
        self.data['endBlock'] = endBlock
        self.data['isHeadExtent'] = isHeadExtent
        self.data['ordinal'] = ordinal
        self.data['reason'] = reason
        self.data['startBlock'] = startBlock
        self.data['vmfsUuid'] = vmfsUuid
    
    
    @property
    def device(self):
        '''The device information
        '''
        return self.data['device']

    @property
    def devicePath(self):
        '''The device path of an VMFS extent
        '''
        return self.data['devicePath']

    @property
    def endBlock(self):
        '''Index of the last block that this extent provides.
        '''
        return self.data['endBlock']

    @property
    def isHeadExtent(self):
        '''Is this a copy of the head extent of the VMFS volume?
        '''
        return self.data['isHeadExtent']

    @property
    def ordinal(self):
        '''A number indicating the order of an extent in a volume. An extent with a lower
        ordinal value than another extent provides a range of blocks to a volume
        at an earlier block address range. Extents with the same ordinal provide
        the same range of blocks to a volume. A zero ordinal indicates that the
        extent is a head extent.
        '''
        return self.data['ordinal']

    @property
    def reason(self):
        '''Reason as to why the partition is marked as copy of a VMFS volume's extent.
        Possible reasons are the disk id is not matching with what the scsi inq is
        saying or disk uuid is not matching
        '''
        return self.data['reason']

    @property
    def startBlock(self):
        '''Index of the first block that this extent provides.
        '''
        return self.data['startBlock']

    @property
    def vmfsUuid(self):
        '''The UUID of the VMFS volume read from to the partition.
        '''
        return self.data['vmfsUuid']

