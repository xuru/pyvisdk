
from pyvisdk.do.description import Description
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ExtendedDescription(Description):
    '''
    '''
    
    def __init__(self, messageArg, messageCatalogKeyPrefix):
        # MUST define these
        super(ExtendedDescription, self).__init__()
    
        self.data['messageArg'] = messageArg
        self.data['messageCatalogKeyPrefix'] = messageCatalogKeyPrefix
    
    
    @property
    def messageArg(self):
        '''Provides named arguments that can be used to localize the message in the catalog.
        '''
        return self.data['messageArg']

    @property
    def messageCatalogKeyPrefix(self):
        '''Key to the localized message string in the catalog. If the localized string
        contains parameters, values to the parameters will be provided in
        #messageArg. E.g: If the message in the catalog is "IP address is
        {address}", value for "address" will be provided by #messageArg. Both
        summary and label in Description will have a corresponding entry in the
        message catalog with the keys .summary and .label respectively.
        Description.summary and Description.label will contain the strings in
        server locale.
        '''
        return self.data['messageCatalogKeyPrefix']

