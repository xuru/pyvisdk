
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class MissingProperty(DynamicData):
    '''Used for reporting properties for which values could not be retrieved.
    '''
    
    def __init__(self, fault, path):
        # MUST define these
        super(MissingProperty, self).__init__()
    
        self.data['fault'] = fault
        self.data['path'] = path
    
    
    @property
    def fault(self):
        '''Fault describing the failure to retrieve the property value.
        '''
        return self.data['fault']

    @property
    def path(self):
        '''Property for which a value could not be retrieved
        '''
        return self.data['path']

