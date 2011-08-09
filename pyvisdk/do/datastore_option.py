
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DatastoreOption(DynamicData):
    '''The DatastoreOption data object describes datastore options for a virtual machine.
    '''
    
    def __init__(self, unsupportedVolumes):
        # MUST define these
        super(DatastoreOption, self).__init__()
    
        self.data['unsupportedVolumes'] = unsupportedVolumes
    
    
    @property
    def unsupportedVolumes(self):
        '''The type of file system volumes on which this virtual machine cannot have its disk
        and configuration files.
        '''
        return self.data['unsupportedVolumes']

