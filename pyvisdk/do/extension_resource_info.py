
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ExtensionResourceInfo(DynamicData):
    '''This data object encapsulates the message resources for all locales.
    '''
    
    def __init__(self, data, locale, module):
        # MUST define these
        super(ExtensionResourceInfo, self).__init__()
    
        self.data['data'] = data
        self.data['locale'] = locale
        self.data['module'] = module
    
    
    @property
    def data(self):
        '''
        '''
        return self.data['data']

    @property
    def locale(self):
        '''
        '''
        return self.data['locale']

    @property
    def module(self):
        '''Module for a resource type and other message or fault resources. Examples: "task"
        for task, "event" for event and "auth" for "privilege".
        '''
        return self.data['module']

