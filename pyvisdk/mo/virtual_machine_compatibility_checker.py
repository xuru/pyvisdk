
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineCompatibilityChecker(BaseEntity):
    '''A singleton managed object that can answer questions about compatibility of a
    virtual machine with a host.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.VirtualMachineCompatibilityChecker):
        super(VirtualMachineCompatibilityChecker, self).__init__(core, name=name, ref=ref, type=type)

    

    
    
    def CheckCompatibility_Task(self, vm, host=None, pool=None, testType=None):
        '''Tests whether or not a virtual machine could be placed on the given host in the
        given resource pool.
        
        :param vm: The virtual machine we'd like to place.
        
        :param host: The host we would like the virtual machine to execute on. The host parameter may be left unset if the compute resource associated with the pool represents a stand-alone host or a DRS-enabled cluster. In the former case the stand-alone host is used. In the latter case, each connected host in the cluster that is not in maintenance mode is tested. If the virtual machine is a template then either this parameter or the pool parameter must be set.
        
        :param pool: The resource pool we would like the virtual machine to reside in. If the pool parameter is left unset, then the virtual machine's current pool is assumed. If the virtual machine is a template then either this parameter or the host parameter must be set.
        
        :param testType: The set of tests to run. If this argument is not set, all tests will be run. See CheckTestType for possible values.
        
        '''
        return self.delegate("CheckCompatibility_Task")(vm, host, pool, testType)