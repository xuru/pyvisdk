
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ExtensionServerInfo(DynamicData):
    '''This data object type describes a server for the extension.
    '''
    
    def __init__(self, adminEmail, company, description, serverThumbprint, type, url):
        # MUST define these
        super(ExtensionServerInfo, self).__init__()
    
        self.data['adminEmail'] = adminEmail
        self.data['company'] = company
        self.data['description'] = description
        self.data['serverThumbprint'] = serverThumbprint
        self.data['type'] = type
        self.data['url'] = url
    
    
    @property
    def adminEmail(self):
        '''Extension administrator email addresses.
        '''
        return self.data['adminEmail']

    @property
    def company(self):
        '''Company information.
        '''
        return self.data['company']

    @property
    def description(self):
        '''Server description.
        '''
        return self.data['description']

    @property
    def serverThumbprint(self):
        '''Thumbprint of the extension server certificate presented to clients
        '''
        return self.data['serverThumbprint']

    @property
    def type(self):
        '''Type of server (examples may include SOAP, REST, HTTP, etc.).
        '''
        return self.data['type']

    @property
    def url(self):
        '''Server url.
        '''
        return self.data['url']

