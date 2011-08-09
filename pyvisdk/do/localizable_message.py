
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LocalizableMessage(DynamicData):
    '''
    '''
    
    def __init__(self, arg, key, message):
        # MUST define these
        super(LocalizableMessage, self).__init__()
    
        self.data['arg'] = arg
        self.data['key'] = key
        self.data['message'] = message
    
    
    @property
    def arg(self):
        '''If the localized message contains variables, messageArg will provide the values
        for the arguments. e.g: If the message is "IP address is {address}", value
        for "address" will be provided by #arg.
        '''
        return self.data['arg']

    @property
    def key(self):
        '''Unique key identifying the message in the localized message catalog.
        '''
        return self.data['key']

    @property
    def message(self):
        '''Message in server locale. This message need not be localized.
        '''
        return self.data['message']

