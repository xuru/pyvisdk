
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomFieldsManager(BaseEntity):
    '''The CustomFieldsManager object is used to add and remove custom fields to
    managed entities.The custom fields values set on managed entities are available
    through the customValue property and through the summary objects for
    VirtualMachine and HostSystem. They are not available directly through this
    managed object.This functionality is only available through VirtualCenter.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.CustomFieldsManager):
        super(CustomFieldsManager, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def field(self):
        '''List of custom fields defined on this server. The fields are sorted by name.'''
        return self.update('field')

    
    
    def AddCustomFieldDef(self, name, moType=None, fieldDefPolicy=None, fieldPolicy=None):
        '''Creates a new custom field. If the moType is specified, the field will only be
        available for that type of managed object.
        
        :param name: The name of the field.
        
        :param moType: The managed object type to which this field will applyVI API 2.5
        
        :param fieldDefPolicy: Privilege policy to apply to FieldDef being createdVI API 2.5
        
        :param fieldPolicy: Privilege policy to apply to instances of fieldVI API 2.5
        
        '''
        return self.delegate("AddCustomFieldDef")(name, moType, fieldDefPolicy, fieldPolicy)
    
    def RemoveCustomFieldDef(self, key):
        '''Removes a custom field. This also removes all values assigned to this custom
        field.
        
        :param key: The unique key for the field definition.
        
        '''
        return self.delegate("RemoveCustomFieldDef")(key)
    
    def RenameCustomFieldDef(self, key, name):
        '''Renames a custom field.
        
        :param key: The unique key for the field definition.
        
        :param name: The new name for the field.
        
        '''
        return self.delegate("RenameCustomFieldDef")(key, name)
    
    def SetField(self, entity, key, value):
        '''Assigns a value to a custom field on an entity.
        
        :param entity: 
        
        :param key: 
        
        :param value: 
        
        '''
        return self.delegate("SetField")(entity, key, value)