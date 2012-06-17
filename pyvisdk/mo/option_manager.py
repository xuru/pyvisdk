
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OptionManager(BaseEntity):
    '''This managed object type is used for managing key/value pair options.* You can
    define options on the fly, in a logical tree using a dot notation for keys. For
    example, "Ethernet.Connection" describes the Connection option as child of the
    Ethernet option. * You can use the queryMethod to retrieve a single property or
    a subset of properties based on the dot notation path.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.OptionManager):
        super(OptionManager, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def setting(self):
        '''A list of the current settings for the key/value pair options.'''
        return self.update('setting')
    @property
    def supportedOption(self):
        '''A list of supported key/value pair options including their type information.'''
        return self.update('supportedOption')

    
    
    def QueryOptions(self, name=None):
        '''Returns a specific node or nodes in the option hierarchy.Returns a specific
        node or nodes in the option hierarchy.Returns a specific node or nodes in the
        option hierarchy.
        
        :param name: 
        
        '''
        return self.delegate("QueryOptions")(name)
    
    def UpdateOptions(self, changedValue):
        '''Updates one or more properties. These properties are changed atomically: either
        all are applied or none are.Updates one or more properties. These properties
        are changed atomically: either all are applied or none are.Updates one or more
        properties. These properties are changed atomically: either all are applied or
        none are.Updates one or more properties. These properties are changed
        atomically: either all are applied or none are.
        
        :param changedValue: 
        
        '''
        return self.delegate("UpdateOptions")(changedValue)