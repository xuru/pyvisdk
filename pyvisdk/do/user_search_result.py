
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class UserSearchResult(DynamicData):
    '''When searching for users, the search results in some additional information. This
        object describes the additional information.
    '''
    
    def __init__(self, fullName, group, principal):
        # MUST define these
        super(UserSearchResult, self).__init__()
    
        self.data['fullName'] = fullName
        self.data['group'] = group
        self.data['principal'] = principal
    
    
    @property
    def fullName(self):
        '''Full name of the user found by the search, or the description of a group, if
        available.
        '''
        return self.data['fullName']

    @property
    def group(self):
        '''If this is true, then the result is a group. If this is false, then the result is
        a user.
        '''
        return self.data['group']

    @property
    def principal(self):
        '''Login name of a user or the name of a group. This key is the user within the
        searched domain.
        '''
        return self.data['principal']

