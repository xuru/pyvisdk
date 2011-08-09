
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PropertyFilterUpdate(DynamicData):
    '''The PropertyFilterUpdate data object type contains a list of updates to data
        visible through a specific filter. Note that if a property changes through
        multiple filters, then a client receives an update for each filter.
    '''
    
    def __init__(self, filter, missingSet, objectSet):
        # MUST define these
        super(PropertyFilterUpdate, self).__init__()
    
        self.data['filter'] = filter
        self.data['missingSet'] = missingSet
        self.data['objectSet'] = objectSet
    
    
    @property
    def filter(self):
        '''Filter that was updated.
        '''
        return self.data['filter']

    @property
    def missingSet(self):
        '''Objects that could not be found on the server, but were specified in a objectSet.
        '''
        return self.data['missingSet']

    @property
    def objectSet(self):
        '''Set of changes to object properties in the filter.
        '''
        return self.data['objectSet']

