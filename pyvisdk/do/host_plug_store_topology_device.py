
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPlugStoreTopologyDevice(DynamicData):
    '''This data object type is an association class that describes a ScsiLun and its
        associated Path objects. The ScsiLun is a Device that is formed from a set
        of Paths.
    '''
    
    def __init__(self, key, lun, path):
        # MUST define these
        super(HostPlugStoreTopologyDevice, self).__init__()
    
        self.data['key'] = key
        self.data['lun'] = lun
        self.data['path'] = path
    
    
    @property
    def key(self):
        '''Linkable identifier.
        '''
        return self.data['key']

    @property
    def lun(self):
        '''The SCSI device corresponding to logical unit.
        '''
        return self.data['lun']

    @property
    def path(self):
        '''The array of paths available to access this LogicalUnit.
        '''
        return self.data['path']

