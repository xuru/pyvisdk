
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ObjectSpec(DynamicData):
    '''Within a PropertyFilterSpec, the ObjectSpec data object type specifies the managed
        object at which the filter begins to collect the managed object references
        and properties specified by the associated PropertySpec set. If the "skip"
        property is present and set to true, then the filter does not check to see
        if the starting object's type matches any of the types listed in the
        associated sets of PropertySpec data objects.If the selectSet property is
        present, then this specifies additional objects to filter. These objects
        are defined by one or more SelectionSpec objects.
    '''
    
    def __init__(self, obj, selectSet, skip):
        # MUST define these
        super(ObjectSpec, self).__init__()
    
        self.data['obj'] = obj
        self.data['selectSet'] = selectSet
        self.data['skip'] = skip
    
    
    @property
    def obj(self):
        '''Starting object.
        '''
        return self.data['obj']

    @property
    def selectSet(self):
        '''Set of selections to specify additional objects to filter.
        '''
        return self.data['selectSet']

    @property
    def skip(self):
        '''Flag to specify whether or not to report this managed object's properties. If the
        flag is true, the filter will not report this managed object's properties.
        '''
        return self.data['skip']

