
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class StorageResourceManager(BaseEntity):
    '''This managed object type provides a way to configure resource usage for storage
    resources.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.StorageResourceManager):
        super(StorageResourceManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    
    
    
    def ConfigureDatastoreIORM_Task(self):
        '''Changes configuration of storage I/O resource management for a given datastore.
        The changes are applied to all the backing storage devices for the datastore.
        Currently we only support storage I/O resource management on VMFS volumes. In
        order to enable storage I/O resource management on a datstore, we require that
        all the hosts that are attached to the datastore support this feature.This
        method is only supported by vCenter server.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("ConfigureDatastoreIORM_Task")()
    
    def QueryIORMConfigOption(self):
        '''Query configuration options for storage I/O resource management.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryIORMConfigOption")()