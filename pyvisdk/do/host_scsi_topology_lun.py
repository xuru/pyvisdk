
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostScsiTopologyLun(DynamicData):
    '''This data object type describes the SCSI logical unit.
    '''
    
    def __init__(self, key, lun, scsiLun):
        # MUST define these
        super(HostScsiTopologyLun, self).__init__()
    
        self.data['key'] = key
        self.data['lun'] = lun
        self.data['scsiLun'] = scsiLun
    
    
    @property
    def key(self):
        '''The identifier for the SCSI Lun
        '''
        return self.data['key']

    @property
    def lun(self):
        '''The logical unit number of the SCSI logical unit.
        '''
        return self.data['lun']

    @property
    def scsiLun(self):
        '''The link to data for this SCSI logical unit.
        '''
        return self.data['scsiLun']

