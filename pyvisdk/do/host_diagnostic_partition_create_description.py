
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDiagnosticPartitionCreateDescription(DynamicData):
    '''The diagnostic partition create description details what will be done to create a
        new diagnostic partition on a disk. It contains a CreateSpec that can be
        submitted to create the partition and information that can be shown to the
        user.
    '''
    
    def __init__(self, diskUuid, layout, spec):
        # MUST define these
        super(HostDiagnosticPartitionCreateDescription, self).__init__()
    
        self.data['diskUuid'] = diskUuid
        self.data['layout'] = layout
        self.data['spec'] = spec
    
    
    @property
    def diskUuid(self):
        '''The UUID of the SCSI disk on which to create the diagnostic partition. This disk
        UUID will match that found in the identification field of the creation
        spec.
        '''
        return self.data['diskUuid']

    @property
    def layout(self):
        '''Layout describing the format of the disk
        '''
        return self.data['layout']

    @property
    def spec(self):
        '''Creation specification for diagnostic partition
        '''
        return self.data['spec']

