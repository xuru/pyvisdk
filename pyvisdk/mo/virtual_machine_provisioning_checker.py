
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineProvisioningChecker(BaseEntity):
    '''A singleton managed object that can answer questions about the feasibility of
        certain provisioning operations.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.VirtualMachineProvisioningChecker):
        # MUST define these
        super(VirtualMachineProvisioningChecker, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def CheckMigrate_Task(self, vm, host):
        '''Tests the feasibility of a proposed MigrateVM_Task operation.

        :param vm: to a VirtualMachine[]The set of virtual machines to analyze for compatibility. All
        virtual machines are assumed to be powered-on for the purposes of this
        operation.

        :param host: to a HostSystem[]The set of hosts to analyze for compatibility. All hosts are
        assumed to be connected and not in maintenence mode for the purposes of
        this operation.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CheckMigrate_Task")(vm,host)
        

    def CheckRelocate_Task(self, vm, host):
        '''Tests the feasibility of a proposed RelocateVM_Task operation.

        :param vm: to a VirtualMachine[]The set of virtual machines to analyze for compatibility. All
        virtual machines are assumed to be powered-on for the purposes of this
        operation.

        :param host: to a HostSystem[]The set of hosts to analyze for compatibility. All hosts are
        assumed to be connected and not in maintenence mode for the purposes of
        this operation.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CheckRelocate_Task")(vm,host)
        

    def QueryVMotionCompatibilityEx_Task(self, vm, host):
        '''Investigates the general VMotion compatibility of a set of virtual machines with a
        set of hosts. The virtual machine may be in any power state. Hosts may be
        in any connection state and also may be in maintenance mode.

        :param vm: to a VirtualMachine[]The set of virtual machines to analyze for compatibility. All
        virtual machines are assumed to be powered-on for the purposes of this
        operation.

        :param host: to a HostSystem[]The set of hosts to analyze for compatibility. All hosts are
        assumed to be connected and not in maintenence mode for the purposes of
        this operation.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("QueryVMotionCompatibilityEx_Task")(vm,host)
        
