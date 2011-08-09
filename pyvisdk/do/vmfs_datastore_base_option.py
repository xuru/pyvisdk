
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmfsDatastoreBaseOption(DynamicData):
    '''Base class that describes a VMFS datastore provisioning option.
    '''
    
    def __init__(self, layout):
        # MUST define these
        super(VmfsDatastoreBaseOption, self).__init__()
    
        self.data['layout'] = layout
    
    
    @property
    def layout(self):
        '''The partition table layout that the disk will have if this provisioning option is
        selected.
        '''
        return self.data['layout']

