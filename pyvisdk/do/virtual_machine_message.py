
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineMessage(DynamicData):
    '''The message data for one message in a sequence of message data.
    '''
    
    def __init__(self, argument, id, text):
        # MUST define these
        super(VirtualMachineMessage, self).__init__()
    
        self.data['argument'] = argument
        self.data['id'] = id
        self.data['text'] = text
    
    
    @property
    def argument(self):
        '''The set of arguments associated with this message.
        '''
        return self.data['argument']

    @property
    def id(self):
        '''A unique identifier for this particular message.
        '''
        return self.data['id']

    @property
    def text(self):
        '''Localized version of the text.
        '''
        return self.data['text']

