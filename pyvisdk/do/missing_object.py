
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class MissingObject(DynamicData):
    '''Used for reporting missing objects that were explicitly referenced by a filter
        spec. In other words, any of the objects referenced in objectSet
    '''
    
    def __init__(self, fault, obj):
        # MUST define these
        super(MissingObject, self).__init__()
    
        self.data['fault'] = fault
        self.data['obj'] = obj
    
    
    @property
    def fault(self):
        '''Fault describing the failure to lookup this object
        '''
        return self.data['fault']

    @property
    def obj(self):
        '''The object that is being reported missing
        '''
        return self.data['obj']

