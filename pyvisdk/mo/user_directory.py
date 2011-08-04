
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class UserDirectory(BaseEntity):
    '''* On a Windows host, RetrieveUserGroups can search from the set of trusted domains
        on the host, including the primary domain of the system. A special domain
        (specified as an empty string - "") refers to the users and groups local
        to the host. * On an ESX Server or a Linux host, the search operates on
        the users and groups defined in the /etc/passwd file. Always specify an
        empty string ("") for the domain argument. If the /etc/passwd file
        contains Sun NIS or NIS+ users and groups, RetrieveUserGroups returns
        information about these accounts as well.
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

