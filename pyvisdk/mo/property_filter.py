
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PropertyFilter(BaseEntity):
    '''The PropertyFilter managed object type defines a filter that controls the
    properties for which a PropertyCollector detects incremental changes. Filters
    are subordinate objects; they are part of the PropertyCollector and do not have
    independent lifetimes. A Filter is automatically destroyed when the session on
    which it was created is closed or the PropertyCollector on which it was created
    is destroyed.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.PropertyFilter):
        super(PropertyFilter, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def partialUpdates(self):
        '''Flag to indicate if a change to a nested property reports only the nested
        change or the entire specified property value. If the value is true, a change
        reports only the nested property. If the value is false, a change reports the
        enclosing property named in the filter.'''
        return self.update('partialUpdates')
    @property
    def spec(self):
        '''Specifications for this filter.'''
        return self.update('spec')

    
    
    def DestroyPropertyFilter(self):
        '''Destroys this filter.Destroys this filter.
        
        '''
        return self.delegate("DestroyPropertyFilter")()