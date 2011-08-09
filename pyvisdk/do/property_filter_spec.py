
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PropertyFilterSpec(DynamicData):
    '''Specify the property data that is included in a filter. A filter can specify part
        of a single managed object, or parts of multiple related managed objects
        in an inventory hierarchy - for example, to collect updates from all
        virtual machines in a given folder.
    '''
    
    def __init__(self, objectSet, propSet, reportMissingObjectsInResults):
        # MUST define these
        super(PropertyFilterSpec, self).__init__()
    
        self.data['objectSet'] = objectSet
        self.data['propSet'] = propSet
        self.data['reportMissingObjectsInResults'] = reportMissingObjectsInResults
    
    
    @property
    def objectSet(self):
        '''Set of specifications that determine the objects to filter.
        '''
        return self.data['objectSet']

    @property
    def propSet(self):
        '''Set of properties to include in the filter, specified for each object type.
        '''
        return self.data['propSet']

    @property
    def reportMissingObjectsInResults(self):
        '''Control how to report missing objects during filter creation.
        '''
        return self.data['reportMissingObjectsInResults']

