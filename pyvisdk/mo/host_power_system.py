
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPowerSystem(BaseEntity):
    '''Managed object responsible for getting and setting host power management
    policies.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostPowerSystem):
        super(HostPowerSystem, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def capability(self):
        '''Power system capabilities object.'''
        return self.update('capability')
    @property
    def info(self):
        '''Power system state info object.'''
        return self.update('info')

    
    
    def ConfigurePowerPolicy(self, key):
        '''Configure host power policy.
        
        :param key: A key from one of the policies in availablePolicy.
        
        '''
        return self.delegate("ConfigurePowerPolicy")(key)