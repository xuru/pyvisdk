
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LocalizationManager(BaseEntity):
    '''Properties
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.LocalizationManager):
        # MUST define these
        super(LocalizationManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def catalog(self):
        '''Fetches the descriptions of all the client-side localization message catalogs
        available for the current session locale.
        '''
        return self.update('catalog')

