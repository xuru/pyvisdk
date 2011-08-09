
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ExtensionClientInfo(DynamicData):
    '''This data object type describes a client of the extension.
    '''
    
    def __init__(self, company, description, type, url, version):
        # MUST define these
        super(ExtensionClientInfo, self).__init__()
    
        self.data['company'] = company
        self.data['description'] = description
        self.data['type'] = type
        self.data['url'] = url
        self.data['version'] = version
    
    
    @property
    def company(self):
        '''Company information.
        '''
        return self.data['company']

    @property
    def description(self):
        '''Description of client.
        '''
        return self.data['description']

    @property
    def type(self):
        '''Type of client (examples may include win32, .net, linux, etc.).
        '''
        return self.data['type']

    @property
    def url(self):
        '''Plugin url.
        '''
        return self.data['url']

    @property
    def version(self):
        '''Client version number as a dot-separated string. For example, "1.0.0"
        '''
        return self.data['version']

