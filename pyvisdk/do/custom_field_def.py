
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomFieldDef(DynamicData):
    '''Describes a custom field.
    '''
    
    def __init__(self, fieldDefPrivileges, fieldInstancePrivileges, key, managedObjectType, name, type):
        # MUST define these
        super(CustomFieldDef, self).__init__()
    
        self.data['fieldDefPrivileges'] = fieldDefPrivileges
        self.data['fieldInstancePrivileges'] = fieldInstancePrivileges
        self.data['key'] = key
        self.data['managedObjectType'] = managedObjectType
        self.data['name'] = name
        self.data['type'] = type
    
    
    @property
    def fieldDefPrivileges(self):
        '''The set of privileges to apply on this field definition
        '''
        return self.data['fieldDefPrivileges']

    @property
    def fieldInstancePrivileges(self):
        '''The set of privileges to apply on instances of this field
        '''
        return self.data['fieldInstancePrivileges']

    @property
    def key(self):
        '''A unique ID used to reference this custom field in assignments. This ID is unique
        for the lifetime of the field (even across rename operations).
        '''
        return self.data['key']

    @property
    def managedObjectType(self):
        '''Type of object for which the field is valid. If not specified, the field is valid
        for all managed objects.
        '''
        return self.data['managedObjectType']

    @property
    def name(self):
        '''Name of the field.
        '''
        return self.data['name']

    @property
    def type(self):
        '''Type of the field.
        '''
        return self.data['type']

