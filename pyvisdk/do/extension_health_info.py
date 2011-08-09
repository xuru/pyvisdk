
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ExtensionHealthInfo(DynamicData):
    '''This data object encapsulates the health specification for the extension.
    '''
    
    def __init__(self, url):
        # MUST define these
        super(ExtensionHealthInfo, self).__init__()
    
        self.data['url'] = url
    
    
    @property
    def url(self):
        '''
        '''
        return self.data['url']

