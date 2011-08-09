
from pyvisdk.do.action import Action
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class SendEmailAction(Action):
    '''This data object type defines an email that is triggered by an alarm. You can use
        any elements of the ActionParameter enumerated list as part of your
        strings to provide information available at runtime.
    '''
    
    def __init__(self, body, ccList, subject, toList):
        # MUST define these
        super(SendEmailAction, self).__init__()
    
        self.data['body'] = body
        self.data['ccList'] = ccList
        self.data['subject'] = subject
        self.data['toList'] = toList
    
    
    @property
    def body(self):
        '''Content of the email notification.
        '''
        return self.data['body']

    @property
    def ccList(self):
        '''A comma-separated list of addresses that are cc'ed on the email notification.
        '''
        return self.data['ccList']

    @property
    def subject(self):
        '''Subject of the email notification.
        '''
        return self.data['subject']

    @property
    def toList(self):
        '''A comma-separated list of addresses to which the email notification is sent.
        '''
        return self.data['toList']

