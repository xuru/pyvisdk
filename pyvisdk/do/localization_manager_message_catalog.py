
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LocalizationManagerMessageCatalog(DynamicData):
    '''Description of an available message catalog
    '''
    
    def __init__(self, catalogName, catalogUri, lastModified, locale, md5sum, moduleName):
        # MUST define these
        super(LocalizationManagerMessageCatalog, self).__init__()
    
        self.data['catalogName'] = catalogName
        self.data['catalogUri'] = catalogUri
        self.data['lastModified'] = lastModified
        self.data['locale'] = locale
        self.data['md5sum'] = md5sum
        self.data['moduleName'] = moduleName
    
    
    @property
    def catalogName(self):
        '''The name of the catalog.
        '''
        return self.data['catalogName']

    @property
    def catalogUri(self):
        '''The URI (relative to the connection URL for the VirtualCenter server itself) from
        which the catalog can be downloaded. The caller will need to augment this
        with a scheme and authority (host and port) to make a complete URL.
        '''
        return self.data['catalogUri']

    @property
    def lastModified(self):
        '''The last-modified time of the catalog file, if available
        '''
        return self.data['lastModified']

    @property
    def locale(self):
        '''The locale for the catalog.
        '''
        return self.data['locale']

    @property
    def md5sum(self):
        '''The checksum of the catalog file, if available
        '''
        return self.data['md5sum']

    @property
    def moduleName(self):
        '''The module or extension that publishes this catalog. The moduleName will be empty
        for the core catalogs for the VirtualCenter server itself.
        '''
        return self.data['moduleName']

