
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class GuestOperationsManager(BaseEntity):
    '''GuestOperationsManager is the managed object that provides APIs to manipulate
    the guest operating system files and process. Each class of APIs is separated
    into its own manager.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.GuestOperationsManager):
        super(GuestOperationsManager, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def authManager(self):
        '''A singleton managed object that provides methods for guest authentication
        operations.'''
        return self.update('authManager')
    @property
    def fileManager(self):
        '''A singleton managed object that provides methods for guest file operations.'''
        return self.update('fileManager')
    @property
    def processManager(self):
        '''A singleton managed object that provides methods for guest process operations.'''
        return self.update('processManager')

    