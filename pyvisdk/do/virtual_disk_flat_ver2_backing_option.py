
from pyvisdk.do.virtual_device_file_backing_option import VirtualDeviceFileBackingOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDiskFlatVer2BackingOption(VirtualDeviceFileBackingOption):
    '''This data object type contains the available options when backing a virtual disk
        using a host file with the flat file format used in VMware Server and in
        ESX Server 2.x and greater. Flat disks are pre-allocated, whereas sparse
        disks are grown as needed.
    '''
    
    def __init__(self, diskMode, eagerlyScrub, growable, hotGrowable, split, thinProvisioned, uuid, writeThrough):
        # MUST define these
        super(VirtualDiskFlatVer2BackingOption, self).__init__()
    
        self.data['diskMode'] = diskMode
        self.data['eagerlyScrub'] = eagerlyScrub
        self.data['growable'] = growable
        self.data['hotGrowable'] = hotGrowable
        self.data['split'] = split
        self.data['thinProvisioned'] = thinProvisioned
        self.data['uuid'] = uuid
        self.data['writeThrough'] = writeThrough
    
    
    @property
    def diskMode(self):
        '''The disk mode. Valid disk modes are: * persistent * independent_persistent *
        independent_nonpersistent
        '''
        return self.data['diskMode']

    @property
    def eagerlyScrub(self):
        '''Flag to indicate if this backing supports eager scrubbing.
        '''
        return self.data['eagerlyScrub']

    @property
    def growable(self):
        '''Indicates whether or not this disk backing can be extended to larger sizes through
        a reconfigure operation.
        '''
        return self.data['growable']

    @property
    def hotGrowable(self):
        '''Indicates whether or not this disk backing can be extended to larger sizes through
        a reconfigure operation while the virtual machine is powered on.
        '''
        return self.data['hotGrowable']

    @property
    def split(self):
        '''Flag to indicate whether or not the host supports allowing the client to select
        whether or not a disk should be split.
        '''
        return self.data['split']

    @property
    def thinProvisioned(self):
        '''Flag to indicate if this backing supports thin-provisioned disks.
        '''
        return self.data['thinProvisioned']

    @property
    def uuid(self):
        '''Flag to indicate whether this backing supports disk UUID property.
        '''
        return self.data['uuid']

    @property
    def writeThrough(self):
        '''Flag to indicate whether or not the host supports allowing the client to select
        "writethrough" as a mode for virtual disks. Typically, this is available
        only for VMware Server Linux hosts.
        '''
        return self.data['writeThrough']

