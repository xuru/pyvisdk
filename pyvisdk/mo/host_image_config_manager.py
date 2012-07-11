
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostImageConfigManager(BaseEntity):
    '''This managed object is the interface for configuration of the ESX software
    image, including properties such as acceptance level. It is currently designed
    to be host agent specific.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostImageConfigManager):
        super(HostImageConfigManager, self).__init__(core, name=name, ref=ref, type=type)

    

    
    
    def HostImageConfigGetAcceptance(self):
        '''Queries the current host acceptance level setting.See HostImageAcceptanceLevel
        
        '''
        return self.delegate("HostImageConfigGetAcceptance")()
    
    def HostImageConfigGetProfile(self):
        '''Queries the current host image profile information.See HostImageProfileSummary
        
        '''
        return self.delegate("HostImageConfigGetProfile")()
    
    def UpdateHostImageAcceptanceLevel(self, newAcceptanceLevel):
        '''Sets the acceptance level of the host image profile.See
        HostImageAcceptanceLevel
        
        :param newAcceptanceLevel: the new AcceptanceLevel to set.See HostImageAcceptanceLevel
        
        '''
        return self.delegate("UpdateHostImageAcceptanceLevel")(newAcceptanceLevel)