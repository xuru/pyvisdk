
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineFileLayout(DynamicData):
    '''Describes the set of files that makes up a virtual machine on disk. The file
        layout is broken into 4 major sections:* Configuration: Files stored in
        the configuration directory * Log: Files stored in the log directory *
        Disk: Files stored relative to a disk configuration file * Snapshot:
        Stored in the snapshot directoryOften the same directory is used for
        configuration, log, disk and snapshots.
    '''
    
    def __init__(self, configFile, disk, logFile, snapshot, swapFile):
        # MUST define these
        super(VirtualMachineFileLayout, self).__init__()
    
        self.data['configFile'] = configFile
        self.data['disk'] = disk
        self.data['logFile'] = logFile
        self.data['snapshot'] = snapshot
        self.data['swapFile'] = swapFile
    
    
    @property
    def configFile(self):
        '''A list of files that makes up the configuration of the virtual machine (excluding
        the .vmx file, since that file is represented in the FileInfo). These are
        relative paths from the configuration directory. A slash is always used as
        a separator. This list will typically include the NVRAM file, but could
        also include other meta-data files.
        '''
        return self.data['configFile']

    @property
    def disk(self):
        '''Files making up each virtual disk.
        '''
        return self.data['disk']

    @property
    def logFile(self):
        '''A list of files stored in the virtual machine's log directory. These are relative
        paths from the logDirectory. A slash is always used as a separator.
        '''
        return self.data['logFile']

    @property
    def snapshot(self):
        '''Files of each snapshot.
        '''
        return self.data['snapshot']

    @property
    def swapFile(self):
        '''The swapfile specific to this virtual machine, if any. This is a complete
        datastore path, not a relative path.
        '''
        return self.data['swapFile']

