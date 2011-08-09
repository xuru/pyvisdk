
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ObjectContent(DynamicData):
    '''The ObjectContent data object type contains the contents retrieved for a single
        managed object.
    '''
    
    def __init__(self, missingSet, obj, propSet):
        # MUST define these
        super(ObjectContent, self).__init__()
    
        self.data['missingSet'] = missingSet
        self.data['obj'] = obj
        self.data['propSet'] = propSet
    
    
    @property
    def missingSet(self):
        '''Properties for which values could not be retrieved and the associated fault.
        '''
        return self.data['missingSet']

    @property
    def obj(self):
        '''Reference to the managed object that contains properties of interest.
        '''
        return self.data['obj']

    @property
    def propSet(self):
        '''Set of name-value pairs for the properties of the managed object.
        '''
        return self.data['propSet']

