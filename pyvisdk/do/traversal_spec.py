
from pyvisdk.do.selection_spec import SelectionSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class TraversalSpec(SelectionSpec):
    '''The TraversalSpec data object type specifies how to derive a new set of objects to
        add to the filter.It specifies a property path whose value is either
        another managed object or an array of managed objects included in the set
        of objects for consideration. This data object can also be named, using
        the "name" field in the base type.
    '''
    
    def __init__(self, path, selectSet, skip, type):
        # MUST define these
        super(TraversalSpec, self).__init__()
    
        self.data['path'] = path
        self.data['selectSet'] = selectSet
        self.data['skip'] = skip
        self.data['type'] = type
    
    
    @property
    def path(self):
        '''Name of the property to use in order to select additional objects.
        '''
        return self.data['path']

    @property
    def selectSet(self):
        '''Optional set of selections to specify additional objects to filter.
        '''
        return self.data['selectSet']

    @property
    def skip(self):
        '''Flag to indicate whether or not to filter the object in the "path" field.
        '''
        return self.data['skip']

    @property
    def type(self):
        '''Name of the object type containing the property.
        '''
        return self.data['type']

