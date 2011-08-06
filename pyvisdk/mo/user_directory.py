
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class UserDirectory(BaseEntity):
    '''The content of the returned results depends on the server environment:
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.UserDirectory):
        # MUST define these
        super(UserDirectory, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def domainList(self):
        '''List of Windows domains available for user searches. On ESX Server or Linux
        systems, this is an empty list.
        '''
        return self.update('domainList')

