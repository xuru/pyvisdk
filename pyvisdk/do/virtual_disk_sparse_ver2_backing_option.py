
from pyvisdk.do.virtual_device_file_backing_option import VirtualDeviceFileBackingOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDiskSparseVer2BackingOption(VirtualDeviceFileBackingOption):
    '''This data object type contains the options available when backing a virtual disk
        using a host file with the sparse file format from VMware Server.
    '''
    
    def __init__(self, diskMode, growable, hotGrowable, split, uuid, writeThrough):
        # MUST define these
        super(VirtualDiskSparseVer2BackingOption, self).__init__()
    
        self.data['diskMode'] = diskMode
        self.data['growable'] = growable
        self.data['hotGrowable'] = hotGrowable
        self.data['split'] = split
        self.data['uuid'] = uuid
        self.data['writeThrough'] = writeThrough
    
    
    @property
    def diskMode(self):
        '''The disk mode. Valid disk modes are: * persistent * nonpersistent * undoable *
        independent_persistent * independent_nonpersistent * append
        '''
        return self.data['diskMode']

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
        whether or not a sparse disk should be split.
        '''
        return self.data['split']

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

