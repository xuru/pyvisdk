
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostMultipathInfoPath(DynamicData):
    '''Path is a storage entity that represents a topological path from a host bus
        adapter to a SCSI logical unit. Each path is unique although each host bus
        adapter/SCSI logical unit pair can have multiple paths.Path objects are
        identified by a key. The specifics of how the key is formatted are
        dependent on the implementation. Example implementations include using
        strings like "vmhba1:0:0:0".
    '''
    
    def __init__(self, adapter, isWorkingPath, key, lun, name, pathState, state, transport):
        # MUST define these
        super(HostMultipathInfoPath, self).__init__()
    
        self.data['adapter'] = adapter
        self.data['isWorkingPath'] = isWorkingPath
        self.data['key'] = key
        self.data['lun'] = lun
        self.data['name'] = name
        self.data['pathState'] = pathState
        self.data['state'] = state
        self.data['transport'] = transport
    
    
    @property
    def adapter(self):
        '''The host bus adapter at one endpoint of this path.
        '''
        return self.data['adapter']

    @property
    def isWorkingPath(self):
        '''A path, managed by a given path selection policy(psp) plugin, is denoted to be a
        Working Path if the psp plugin is likely to select the path for performing
        I/O in the near future.
        '''
        return self.data['isWorkingPath']

    @property
    def key(self):
        '''The identifier of the Path.
        '''
        return self.data['key']

    @property
    def lun(self):
        '''The logical unit at one endpoint of this path.
        '''
        return self.data['lun']

    @property
    def name(self):
        '''Name of path.
        '''
        return self.data['name']

    @property
    def pathState(self):
        '''*
        '''
        return self.data['pathState']

    @property
    def state(self):
        '''The system reported state of the path. Must be one of the values of MultipathState
        '''
        return self.data['state']

    @property
    def transport(self):
        '''Transport information for the target end of the path.
        '''
        return self.data['transport']

