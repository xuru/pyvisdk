
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomFieldsManager(BaseEntity):
    '''The CustomFieldsManager object is used to add and remove custom fields to managed
        entities.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.CustomFieldsManager):
        # MUST define these
        super(CustomFieldsManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def field(self):
        '''
        List of custom fields defined on this server. The fields are sorted by name.
        '''
        return self.update('field')


    def AddCustomFieldDef(self, name):
        '''Creates a new custom field. If the moType is specified, the field will only be
        available for that type of managed object.

        :param name: The name of the field.


        :rtype: CustomFieldDef 

        '''
        
        return self.delegate("AddCustomFieldDef")(name)
        

    def RemoveCustomFieldDef(self, key):
        '''Removes a custom field. This also removes all values assigned to this custom
        field.

        :param key: The unique key for the field definition.

        '''
        
        return self.delegate("RemoveCustomFieldDef")(key)
        

    def RenameCustomFieldDef(self, name, key):
        '''Renames a custom field.

        :param name: The new name for the field.

        :param key: The unique key for the field definition.

        '''
        
        return self.delegate("RenameCustomFieldDef")(name,key)
        

    def SetField(self, value, key):
        '''Assigns a value to a custom field on an entity.

        :param value: 

        :param key: 

        '''
        
        return self.delegate("SetField")(value,key)
        
