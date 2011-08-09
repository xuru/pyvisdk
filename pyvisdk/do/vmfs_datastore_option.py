
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmfsDatastoreOption(DynamicData):
    '''VMFS datastore provisioning option that can be applied on a disk. VMFS datastores
        can be created or have their capacity increased using storage from a disk.
        There are often multiple ways in which extents can be allocated on a disk.
        Each instance of this structure represents one of the possible options
        that can be applied to provisiong VMFS datastore storage. Only options
        that follow ESX Server best practice guidelines will be presented.
    '''
    
    def __init__(self, info, spec):
        # MUST define these
        super(VmfsDatastoreOption, self).__init__()
    
        self.data['info'] = info
        self.data['spec'] = spec
    
    
    @property
    def info(self):
        '''Information about this VMFS datastore provisioniing option. This structure
        describes the extent allocation policy represented by this option.
        '''
        return self.data['info']

    @property
    def spec(self):
        '''Specification to create or increase the capacity of a VMFS datastore. This
        property contains a configuration specification that can be applied to
        effect the creation or capacity increase.
        '''
        return self.data['spec']

