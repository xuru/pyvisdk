
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ExtensibleManagedObject(BaseEntity):
    '''ExtensibleManagedObject provides methods and properties that provide access to
    custom fields that may be associated with a managed object. Use the
    CustomFieldsManager to define custom fields. The CustomFieldsManager handles
    the entire list of custom fields on a server. You can can specify the object
    type to which a particular custom field applies by setting its
    managedObjectType. (If you do not set a managed object type for a custom field
    definition, the field applies to all managed objects.)'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.ExtensibleManagedObject):
        super(ExtensibleManagedObject, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def availableField(self):
        '''List of custom field definitions that are valid for the object's type. The
        fields are sorted by name.'''
        return self.update('availableField')
    @property
    def value(self):
        '''List of custom field values. Each value uses a key to associate an instance of
        a CustomFieldStringValue with a custom field definition.'''
        return self.update('value')

    
    
    def setCustomValue(self, key, value):
        '''Assigns a value to a custom field. The setCustomValue method requires whichever
        updatePrivilege is defined as one of the fieldInstancePrivileges for the
        CustomFieldDef whose value is being changed.
        
        :param key: The name of the field whose value is to be updated.
        
        :param value: Value to be assigned to the custom field.
        
        '''
        return self.delegate("setCustomValue")(key, value)