
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ExtensibleManagedObject(BaseEntity):
    '''
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.ExtensibleManagedObject):
        # MUST define these
        super(ExtensibleManagedObject, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def availableField(self):
        '''List of custom field definitions that are valid for the object's type. The fields
        are sorted by name.
        '''
        return self.update('availableField')

    @property
    def value(self):
        '''List of custom field values. Each value uses a key to associate an instance of a
        CustomFieldStringValue with a custom field definition.
        '''
        return self.update('value')

