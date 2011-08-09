
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineQuestionInfo(DynamicData):
    '''This data object type describes the question that is currently blocking a virtual
        machine.
    '''
    
    def __init__(self, choice, id, message, text):
        # MUST define these
        super(VirtualMachineQuestionInfo, self).__init__()
    
        self.data['choice'] = choice
        self.data['id'] = id
        self.data['message'] = message
        self.data['text'] = text
    
    
    @property
    def choice(self):
        '''List of key-value pairs that specify possible answers.
        '''
        return self.data['choice']

    @property
    def id(self):
        '''Identifier with an opaque value that specifies the pending question.
        '''
        return self.data['id']

    @property
    def message(self):
        '''The message data for the individual messages that comprise the question. Only
        available on servers that support localization.
        '''
        return self.data['message']

    @property
    def text(self):
        '''Text that describes the pending question.
        '''
        return self.data['text']

