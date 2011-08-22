
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.base_entity import BaseEntity
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
    
    
    
    def QueryOptions(self):
        '''Returns a specific node or nodes in the option hierarchy.This method might
        require any of the following privileges depending on where the property fits in
        the inventory tree.* System.View on the root folder, if this is used to read
        settings in the "client" subtree. * System.Read on the root folder, if this is
        used to read all settings or any settings beside those in the "client" subtree.
        * System.Read on the host, if this is used to read the advanced options for a
        host configuration.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryOptions")()
    
    def UpdateOptions(self):
        '''Updates one or more properties. These properties are changed atomically: either
        all are applied or none are.A nested option setting can be named using a dot
        notation; for example, system.cacheSize.This method might require any of the
        following privileges depending on where the property fits in the inventory
        tree.* Global.Settings on the root folder, if this is used to modify the
        settings in the service node. * Host.Config.AdvancedConfig on the host, if this
        is used to set the advanced options in the host configuration.
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdateOptions")()