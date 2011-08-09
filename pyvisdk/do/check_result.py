
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CheckResult(DynamicData):
    '''The result of a call to any of the methods in either
        VirtualMachineCompatibilityChecker or VirtualMachineProvisioningChecker.
    '''
    
    def __init__(self, error, host, vm, warning):
        # MUST define these
        super(CheckResult, self).__init__()
    
        self.data['error'] = error
        self.data['host'] = host
        self.data['vm'] = vm
        self.data['warning'] = warning
    
    
    @property
    def error(self):
        '''A list of faults representing problems which are fatal to the operation. For
        VirtualMachineProvisioningChecker an error means that the given
        provisioning operation would fail. For VirtualMachineCompatibilityChecker
        an error means that either a power-on of this virtual machine would fail,
        or that the virtual machine would not run correctly once powered-on.
        '''
        return self.data['error']

    @property
    def host(self):
        '''The host involved in the testing.
        '''
        return self.data['host']

    @property
    def vm(self):
        '''The virtual machine involved in the testing.
        '''
        return self.data['vm']

    @property
    def warning(self):
        '''A list of faults representing problems which may require attention, but which are
        not fatal.
        '''
        return self.data['warning']

