
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPatchManagerLocator(DynamicData):
    '''
    '''
    
    def __init__(self, proxy, url):
        # MUST define these
        super(HostPatchManagerLocator, self).__init__()
    
        self.data['proxy'] = proxy
        self.data['url'] = url
    
    
    @property
    def proxy(self):
        '''The proxy setting required to access the URL from the host. If unset, a direct URL
        connection will be attempted.
        '''
        return self.data['proxy']

    @property
    def url(self):
        '''The URL that will be used to access the patch repository.
        '''
        return self.data['url']

