
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PropertyChange(DynamicData):
    '''Describes a change to a property.
    '''
    
    def __init__(self, name, op):
        # MUST define these
        super(PropertyChange, self).__init__()
    
        self.data['name'] = name
        self.data['op'] = op
    
    
    @property
    def name(self):
        '''Property or nested property to which the change applies. Nested properties are
        specified by paths; for example, * foo.bar * foo.arProp["key val"] *
        foo.arProp["key val"].baz
        '''
        return self.data['name']

    @property
    def op(self):
        '''Change operation for the property. Valid values are:
        '''
        return self.data['op']

