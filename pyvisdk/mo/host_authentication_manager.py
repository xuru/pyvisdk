
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostAuthenticationManager(BaseEntity):
    '''There are two approaches that you can use to add an ESX host to or remove a host
        from an Active Directory domain.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostAuthenticationManager):
        # MUST define these
        super(HostAuthenticationManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def info(self):
        '''Information about Active Directory membership.
        '''
        return self.update('info')

    @property
    def supportedStore(self):
        '''An array that can contain managed object references to local and Active Directory
        authentication managed objects.
        '''
        return self.update('supportedStore')

