
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineSnapshot(ExtensibleManagedObject):
    '''The Snapshot managed object type specifies the interface to individual
    snapshots of a virtual machine. Although these are managed objects, they are
    subordinate to their virtual machine.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.VirtualMachineSnapshot):
        super(VirtualMachineSnapshot, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def childSnapshot(self):
        '''All snapshots for which this snapshot is the parent.'''
        return self.update('childSnapshot')
    @property
    def config(self):
        '''Information about the configuration of this virtual machine when this snapshot
    was taken.'''
        return self.update('config')
    
    
    
    def RemoveSnapshot_Task(self):
        '''Removes this snapshot and deletes any associated storage.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("RemoveSnapshot_Task")()
    
    def RenameSnapshot(self):
        '''Rename this snapshot with either a new name or a new description or both. At
        least one of these must be specified when calling the rename method.
        :rtype: None
        :returns: 
        '''
        return self.delegate("RenameSnapshot")()
    
    def RevertToSnapshot_Task(self):
        '''Change the execution state of the virtual machine to the state of this
        snapshot.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("RevertToSnapshot_Task")()