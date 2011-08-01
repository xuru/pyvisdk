
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OptionManager(BaseEntity):
    '''This managed object type is used for managing key/value pair options.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.OptionManager):
        # MUST define these
        super(OptionManager, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def QueryOptions(self):
        '''Returns a specific node or nodes in the option hierarchy.This method might require
        any of the following privileges depending on where the property fits in
        the inventory tree.

        :rtype: OptionValue[] 

        '''
        
        return self.delegate("QueryOptions")()
        

    def UpdateOptions(self, changedValue):
        '''Updates one or more properties. These properties are changed atomically: either
        all are applied or none are.A nested option setting can be named using a
        dot notation; for example, system.cacheSize.This method might require any
        of the following privileges depending on where the property fits in the
        inventory tree.

        :param changedValue: 

        '''
        
        return self.delegate("UpdateOptions")(changedValue)
        
