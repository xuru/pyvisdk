
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomFieldsManager(BaseEntity):
    '''The CustomFieldsManager object is used to add and remove custom fields to managed
        entities.The custom fields values set on managed entities are available
        through the customValue property and through the summary objects for
        VirtualMachine and HostSystem. They are not available directly through
        this managed object.This functionality is only available through
        VirtualCenter.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.CustomFieldsManager):
        # MUST define these
        super(CustomFieldsManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def field(self):
        '''List of custom fields defined on this server. The fields are sorted by name.
        '''
        return self.update('field')


    def AddCustomFieldDef(self, entity):
        '''Creates a new custom field. If the moType is specified, the field will only be
        available for that type of managed object.

        :param entity: to a ManagedEntity

        '''
        
        return self.delegate("AddCustomFieldDef")(entity)
        

    def RemoveCustomFieldDef(self, entity):
        '''Removes a custom field. This also removes all values assigned to this custom
        field.

        :param entity: to a ManagedEntity

        '''
        
        return self.delegate("RemoveCustomFieldDef")(entity)
        

    def RenameCustomFieldDef(self, entity):
        '''Renames a custom field.

        :param entity: to a ManagedEntity

        '''
        
        return self.delegate("RenameCustomFieldDef")(entity)
        

    def SetField(self, entity):
        '''Assigns a value to a custom field on an entity.

        :param entity: to a ManagedEntity

        '''
        
        return self.delegate("SetField")(entity)
        
