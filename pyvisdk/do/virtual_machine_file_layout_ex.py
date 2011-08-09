
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineFileLayoutEx(DynamicData):
    '''Detailed description of files that make up a virtual machine on disk. The file
        layout is broken into 4 major sections:* Configuration: Files stored in
        the configuration directory * Log: Files stored in the log directory *
        Disk: Files stored relative to a disk configuration file * Snapshot:
        Stored in the snapshot directoryOften the same directory is used for
        configuration, log, disk and snapshots.
    '''
    
    def __init__(self, disk, file, snapshot, timestamp):
        # MUST define these
        super(VirtualMachineFileLayoutEx, self).__init__()
    
        self.data['disk'] = disk
        self.data['file'] = file
        self.data['snapshot'] = snapshot
        self.data['timestamp'] = timestamp
    
    
    @property
    def disk(self):
        '''Layout of each virtual disk attached to the virtual machine.
        '''
        return self.data['disk']

    @property
    def file(self):
        '''Information about all the files that constitute the virtual machine including
        configuration files, disks, swap file, suspend file, log files, core
        files, memory file etc. VirtualMachineFileLayoutExFileType lists the
        different file-types that make a virtual machine.
        '''
        return self.data['file']

    @property
    def snapshot(self):
        '''Layout of each snapshot of the virtual machine.
        '''
        return self.data['snapshot']

    @property
    def timestamp(self):
        '''Time when values in this structure were last updated.
        '''
        return self.data['timestamp']

