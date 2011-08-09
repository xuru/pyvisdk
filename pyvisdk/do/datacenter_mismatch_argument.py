
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DatacenterMismatchArgument(DynamicData):
    '''An input entity argument that belongs to a mismatched datacenter.
    '''
    
    def __init__(self, entity, inputDatacenter):
        # MUST define these
        super(DatacenterMismatchArgument, self).__init__()
    
        self.data['entity'] = entity
        self.data['inputDatacenter'] = inputDatacenter
    
    
    @property
    def entity(self):
        '''The invalid input entity.
        '''
        return self.data['entity']

    @property
    def inputDatacenter(self):
        '''The datacenter for this entity.
        '''
        return self.data['inputDatacenter']

