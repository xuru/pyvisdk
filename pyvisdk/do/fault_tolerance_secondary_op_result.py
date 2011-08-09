
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class FaultToleranceSecondaryOpResult(DynamicData):
    '''FaultToleranceSecondaryOpResult is a data object that reports on the outcome of
        the CreateSecondaryVM_Task or EnableSecondaryVM_Task operation.
    '''
    
    def __init__(self, powerOnAttempted, powerOnResult, vm):
        # MUST define these
        super(FaultToleranceSecondaryOpResult, self).__init__()
    
        self.data['powerOnAttempted'] = powerOnAttempted
        self.data['powerOnResult'] = powerOnResult
        self.data['vm'] = vm
    
    
    @property
    def powerOnAttempted(self):
        '''Whether an attempt was made to power on the secondary. If an attempt was made,
        powerOnResult will report the status of this attempt.
        '''
        return self.data['powerOnAttempted']

    @property
    def powerOnResult(self):
        '''The powerOnResult property reports the outcome of powering on the Secondary
        VirtualMachine if a power on was required. A power on will be attempted if
        the Primary Virtual Machine is powered on when the operation is performed.
        This object is only reported if powerOnAttempted is true. If the outcome
        of the power-on attempt is not successful, the returned
        ClusterPowerOnVmResult object will include an instance of
        ClusterNotAttemptedVmInfo whereas if the attempt was successful, then an
        instance of ClusterAttemptedVmInfo is returned. When
        ClusterAttemptedVmInfo is returned, its task property is only set if the
        cluster is a HA-only cluster.
        '''
        return self.data['powerOnResult']

    @property
    def vm(self):
        '''The Secondary VirtualMachine
        '''
        return self.data['vm']

