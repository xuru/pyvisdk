
from pyvisdk.do.user_search_result import UserSearchResult
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PosixUserSearchResult(UserSearchResult):
    '''Searching for users and groups on POSIX systems provides User ID and Group ID
        information, in addition to that defined in UserSearchResult.
    '''
    
    def __init__(self, id, shellAccess):
        # MUST define these
        super(PosixUserSearchResult, self).__init__()
    
        self.data['id'] = id
        self.data['shellAccess'] = shellAccess
    
    
    @property
    def id(self):
        '''If the search result is for a user, then id refers to User ID. For a group, the
        value of Group ID is assigned to id.
        '''
        return self.data['id']

    @property
    def shellAccess(self):
        '''If the search result is for a user, shellAccess indicates whether shell access has
        been granted or not.
        '''
        return self.data['shellAccess']

