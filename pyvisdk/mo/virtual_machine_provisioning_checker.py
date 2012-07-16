
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

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

    

    
    
    def CheckMigrate_Task(self, vm, host=None, pool=None, state=None, testType=None):
        '''Tests the feasibility of a proposed MigrateVM_Task operation.
        
        :param vm: The virtual machine we propose to migrate.
        
        :param host: The target host on which the virtual machines will run. The host parameter may be left unset if the compute resource associated with the target pool represents a stand-alone host or a DRS-enabled cluster. In the former case the stand-alone host is used as the target host. In the latter case, each connected host in the cluster that is not in maintenance mode is tested as a target host. If the virtual machine is a template then either this parameter or the pool parameter must be set.
        
        :param pool: The target resource pool for the virtual machines. If the pool parameter is left unset, the target pool for each particular virtual machine's migration will be that virtual machine's current pool. If the virtual machine is a template then either this parameter or the host parameter must be set.
        
        :param state: The power state that the virtual machines must have. If this argument is not set, each virtual machine is evaluated according to its current power state.
        
        :param testType: The set of tests to run. If this argument is not set, all tests will be run.
        
        '''
        return self.delegate("CheckMigrate_Task")(vm, host, pool, state, testType)
    
    def CheckRelocate_Task(self, vm, spec, testType=None):
        '''Tests the feasibility of a proposed RelocateVM_Task operation.
        
        :param vm: The virtual machine we propose to relocate.
        
        :param spec: The specification of where to relocate the virtual machine. In cases where DRS would automatically select a host, all potential hosts are tested against.
        
        :param testType: 
        
        '''
        return self.delegate("CheckRelocate_Task")(vm, spec, testType)
    
    def QueryVMotionCompatibilityEx_Task(self, vm, host):
        '''Investigates the general VMotion compatibility of a set of virtual machines
        with a set of hosts. The virtual machine may be in any power state. Hosts may
        be in any connection state and also may be in maintenance mode.
        
        :param vm: The set of virtual machines to analyze for compatibility. All virtual machines are assumed to be powered-on for the purposes of this operation.
        
        :param host: The set of hosts to analyze for compatibility. All hosts are assumed to be connected and not in maintenence mode for the purposes of this operation.
        
        '''
        return self.delegate("QueryVMotionCompatibilityEx_Task")(vm, host)