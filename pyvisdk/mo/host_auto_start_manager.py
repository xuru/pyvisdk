
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostAutoStartManager(BaseEntity):
    '''The AutoStartManager allows clients to invoke and set up the auto-start/auto-
    stop order of virtual machines on a single host. Virtual machines configured to
    use auto-start are automatically started or stopped when the host is started or
    shut down. The AutoStartManager is available when clients connect directly to a
    host, such as an ESX Server machine or through VirtualCenter.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostAutoStartManager):
        super(HostAutoStartManager, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def config(self):
        ''''''
        return self.update('config')

    
    
    def AutoStartPowerOff(self):
        '''Powers-off virtual machines according to the current AutoStart configuration
        .Powers-off virtual machines according to the current AutoStart configuration.
        
        '''
        return self.delegate("AutoStartPowerOff")()
    
    def AutoStartPowerOn(self):
        '''Powers-on virtual machines according to the current AutoStart configuration
        .Powers-on virtual machines according to the current AutoStart configuration.
        
        '''
        return self.delegate("AutoStartPowerOn")()
    
    def ReconfigureAutostart(self, spec):
        '''Changes the power-on or power-off sequence and system defaults. The
        specification is an incremental change to the current configuration.Changes the
        power-on or power-off sequence and system defaults. The specification is an
        incremental change to the current configuration.Changes the power-on or power-
        off sequence and system defaults. The specification is an incremental change to
        the current configuration.Changes the power-on or power-off sequence and system
        defaults. The specification is an incremental change to the current
        configuration.
        
        :param spec: List of changes to defaults and auto-start/auto-stop order.
        
        '''
        return self.delegate("ReconfigureAutostart")(spec)