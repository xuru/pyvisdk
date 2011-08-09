
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineFileInfo(DynamicData):
    '''The FileInfo data object type contains the locations of virtual machine files
        other than the virtual disk files. The configurable parameters are all in
        the FileInfo object.The object also contains a FileLayout object that
        returns a complete list of additional files that makes up the virtual
        machine configuration. This is a read-only structure and is returned when
        the configuration is read. This is ignored during configuration and can be
        left out.
    '''
    
    def __init__(self, logDirectory, snapshotDirectory, suspendDirectory, vmPathName):
        # MUST define these
        super(VirtualMachineFileInfo, self).__init__()
    
        self.data['logDirectory'] = logDirectory
        self.data['snapshotDirectory'] = snapshotDirectory
        self.data['suspendDirectory'] = suspendDirectory
        self.data['vmPathName'] = vmPathName
    
    
    @property
    def logDirectory(self):
        '''Directory to store the log files for the virtual machine. If not specified, this
        defaults to the same directory as the configuration file,
        '''
        return self.data['logDirectory']

    @property
    def snapshotDirectory(self):
        '''Path name of the directory that typically holds suspend, redo, or snapshot files
        belonging to the virtual machine. This path name defaults to the same
        directory as the configuration file.
        '''
        return self.data['snapshotDirectory']

    @property
    def suspendDirectory(self):
        '''Some products allow the suspend directory to be different than the snapshot
        directory. On products where this is not possible, setting of this
        property is ignored.
        '''
        return self.data['suspendDirectory']

    @property
    def vmPathName(self):
        '''Path name to the configuration file for the virtual machine, e.g., the .vmx file.
        This also implicitly defines the configuration directory.
        '''
        return self.data['vmPathName']

