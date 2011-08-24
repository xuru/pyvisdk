
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
    
    
    
    def AddCustomFieldDef(self):
        '''Creates a new custom field. If the moType is specified, the field will only be
        available for that type of managed object.
        :rtype: 
        :returns: 
        '''
        return self.delegate("AddCustomFieldDef")()
    
    def RemoveCustomFieldDef(self):
        '''Removes a custom field. This also removes all values assigned to this custom
        field.
        :rtype: None
        :returns: 
        '''
        return self.delegate("RemoveCustomFieldDef")()
    
    def RenameCustomFieldDef(self):
        '''Renames a custom field.
        :rtype: None
        :returns: 
        '''
        return self.delegate("RenameCustomFieldDef")()
    
    def SetField(self):
        '''Assigns a value to a custom field on an entity.
        :rtype: None
        :returns: 
        '''
        return self.delegate("SetField")()