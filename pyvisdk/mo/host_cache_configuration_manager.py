
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostCacheConfigurationManager(BaseEntity):
    '''Solid state drive Cache Configuration Manager. This is a managed object which
    provides access to ESX performance tuning features using solid state drive
    based cache.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostCacheConfigurationManager):
        super(HostCacheConfigurationManager, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def cacheConfigurationInfo(self):
        '''The swap performance configuration for the ESX host. This includes
        configuration information for each datastore enabled for this purpose.'''
        return self.update('cacheConfigurationInfo')

    
    
    def ConfigureHostCache_Task(self, spec):
        '''Configure host cache/swap performance enhancement.
        
        :param spec: Specification for solid state drive cache configuration.
        
        '''
        return self.delegate("ConfigureHostCache_Task")(spec)