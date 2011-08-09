
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class UserSession(DynamicData):
    '''Information about a current user session.
    '''
    
    def __init__(self, fullName, key, lastActiveTime, locale, loginTime, messageLocale, userName):
        # MUST define these
        super(UserSession, self).__init__()
    
        self.data['fullName'] = fullName
        self.data['key'] = key
        self.data['lastActiveTime'] = lastActiveTime
        self.data['locale'] = locale
        self.data['loginTime'] = loginTime
        self.data['messageLocale'] = messageLocale
        self.data['userName'] = userName
    
    
    @property
    def fullName(self):
        '''The full name of the user, if available.
        '''
        return self.data['fullName']

    @property
    def key(self):
        '''A unique identifier for this session, also known as the session ID.
        '''
        return self.data['key']

    @property
    def lastActiveTime(self):
        '''Timestamp when the user last executed a command.
        '''
        return self.data['lastActiveTime']

    @property
    def locale(self):
        '''The locale for the session used for data formatting and preferred for messages.
        '''
        return self.data['locale']

    @property
    def loginTime(self):
        '''Timestamp when the user last logged on to the server.
        '''
        return self.data['loginTime']

    @property
    def messageLocale(self):
        '''The locale used for messages for the session. If there are no localized messages
        for the user-specified locale, then the server determines this locale.
        '''
        return self.data['messageLocale']

    @property
    def userName(self):
        '''The user name represented by this session.
        '''
        return self.data['userName']

