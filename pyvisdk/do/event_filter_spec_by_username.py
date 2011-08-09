
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class EventFilterSpecByUsername(DynamicData):
    '''This option specifies users used to filter event history.
    '''
    
    def __init__(self, systemUser, userList):
        # MUST define these
        super(EventFilterSpecByUsername, self).__init__()
    
        self.data['systemUser'] = systemUser
        self.data['userList'] = userList
    
    
    @property
    def systemUser(self):
        '''filter by system user true for system user event
        '''
        return self.data['systemUser']

    @property
    def userList(self):
        '''all interested username list If this property is not set, then all regular user
        events are collected
        '''
        return self.data['userList']

