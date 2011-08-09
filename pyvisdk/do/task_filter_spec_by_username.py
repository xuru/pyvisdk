
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class TaskFilterSpecByUsername(DynamicData):
    '''This data object type enables you to filter task history according to the users
        who performed the tasks.
    '''
    
    def __init__(self, systemUser, userList):
        # MUST define these
        super(TaskFilterSpecByUsername, self).__init__()
    
        self.data['systemUser'] = systemUser
        self.data['userList'] = userList
    
    
    @property
    def systemUser(self):
        '''Whether or not to filter by system user. If set to true, filters for system user
        event.
        '''
        return self.data['systemUser']

    @property
    def userList(self):
        '''Specifies the username list to use in the filter. If not set, then all regular
        user tasks are collected.
        '''
        return self.data['userList']

