
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineProvisioningChecker(BaseEntity):
    '''A singleton managed object that can answer questions about the feasibility of
    certain provisioning operations.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.VirtualMachineProvisioningChecker):
        super(VirtualMachineProvisioningChecker, self).__init__(core, name=name, ref=ref, type=type)
    
    
    
    
    
    def CheckMigrate_Task(self):
        '''Tests the feasibility of a proposed MigrateVM_Task operation.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("CheckMigrate_Task")()
    
    def CheckRelocate_Task(self):
        '''Tests the feasibility of a proposed RelocateVM_Task operation.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("CheckRelocate_Task")()
    
    def QueryVMotionCompatibilityEx_Task(self):
        '''Investigates the general VMotion compatibility of a set of virtual machines
        with a set of hosts. The virtual machine may be in any power state. Hosts may
        be in any connection state and also may be in maintenance mode.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("QueryVMotionCompatibilityEx_Task")()