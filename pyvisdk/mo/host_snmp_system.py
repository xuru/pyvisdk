
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostSnmpSystem(BaseEntity):
    '''Properties
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostSnmpSystem):
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
        
