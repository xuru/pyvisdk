
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.folder import Folder

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class StoragePod(Folder):
    '''The StoragePod data object aggregates the storage resources of associated
    Datastore objects into a single storage resource for use by virtual machines.
    The storage services such as Storage DRS (Distributed Resource Scheduling),
    enhance the utility of the storage pod.Use the Folder.CreateStoragePod method
    to create an instance of this object.NOTE: This managed object type and all of
    its methods are experimental and subject to change in future releases.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.StoragePod):
        super(StoragePod, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def podStorageDrsEntry(self):
        '''Storage DRS related attributes of the Storage Pod.'''
        return self.update('podStorageDrsEntry')
    @property
    def summary(self):
        '''Storage pod summary.'''
        return self.update('summary')

    