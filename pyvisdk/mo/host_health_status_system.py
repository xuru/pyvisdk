
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostHealthStatusSystem(BaseEntity):
    '''This managed object manages the health state of the host.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostHealthStatusSystem):
        super(HostHealthStatusSystem, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def runtime(self):
        ''''''
        return self.update('runtime')

    
    
    def RefreshHealthStatusSystem(self):
        '''Refresh the available runtime hardware health information.
        
        '''
        return self.delegate("RefreshHealthStatusSystem")()
    
    def ResetSystemHealthInfo(self):
        '''Resets the state of the sensors of the IPMI subsystem. On certain types of
        hardware IPMI sensor states latch onto unhealthy states and will stay in an
        unhealth state until the sensor state is reset. This method will explicitly
        reset the sensors state.
        
        '''
        return self.delegate("ResetSystemHealthInfo")()