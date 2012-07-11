
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LocalizationManager(BaseEntity):
    '''This managed object type presents all the message catalogs for client-side
    localization of messages.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.LocalizationManager):
        super(LocalizationManager, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def catalog(self):
        '''Fetches the descriptions of all the client-side localization message catalogs
        available for the current session locale.'''
        return self.update('catalog')

    