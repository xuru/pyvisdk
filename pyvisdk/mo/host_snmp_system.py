
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostSnmpSystem(BaseEntity):
    '''Provision the SNMP Version 1,2c agent. This object is a singleton accessed through
        the HostConfigManager object.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostSnmpSystem):
        # MUST define these
        super(HostSnmpSystem, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def SendTestNotification(self):
        '''
        '''
        
        return self.delegate("SendTestNotification")()
        

    def ReconfigureSnmpAgent(self, spec):
        '''

        :param spec: 

        '''
        
        return self.delegate("ReconfigureSnmpAgent")(spec)
        
