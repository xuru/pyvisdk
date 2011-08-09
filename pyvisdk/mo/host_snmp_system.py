
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.base.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostSnmpSystem(BaseEntity):
    '''Provision the SNMP Version 1,2c agent. This object is a singleton accessed through
        the HostConfigManager object.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostSnmpSystem):
        # MUST define these
        super(HostSnmpSystem, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def configuration(self):
        '''VI API 2.5
        '''
        return self.update('configuration')

    @property
    def limits(self):
        '''VI API 2.5
        '''
        return self.update('limits')


    def ReconfigureSnmpAgent(self):
        '''
        '''
        
        return self.delegate("ReconfigureSnmpAgent")()
        

    def SendTestNotification(self):
        '''
        '''
        
        return self.delegate("SendTestNotification")()
        
