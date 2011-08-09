
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineRuntimeInfo(DynamicData):
    '''The RuntimeInfo data object type provides information about the execution state
        and history of a virtual machine.
    '''
    
    def __init__(self, bootTime, cleanPowerOff, connectionState, device, faultToleranceState, host, maxCpuUsage, maxMemoryUsage, memoryOverhead, minRequiredEVCModeKey, needSecondaryReason, numMksConnections, powerState, question, recordReplayState, suspendInterval, suspendTime, toolsInstallerMounted):
        # MUST define these
        super(VirtualMachineRuntimeInfo, self).__init__()
    
        self.data['bootTime'] = bootTime
        self.data['cleanPowerOff'] = cleanPowerOff
        self.data['connectionState'] = connectionState
        self.data['device'] = device
        self.data['faultToleranceState'] = faultToleranceState
        self.data['host'] = host
        self.data['maxCpuUsage'] = maxCpuUsage
        self.data['maxMemoryUsage'] = maxMemoryUsage
        self.data['memoryOverhead'] = memoryOverhead
        self.data['minRequiredEVCModeKey'] = minRequiredEVCModeKey
        self.data['needSecondaryReason'] = needSecondaryReason
        self.data['numMksConnections'] = numMksConnections
        self.data['powerState'] = powerState
        self.data['question'] = question
        self.data['recordReplayState'] = recordReplayState
        self.data['suspendInterval'] = suspendInterval
        self.data['suspendTime'] = suspendTime
        self.data['toolsInstallerMounted'] = toolsInstallerMounted
    
    
    @property
    def bootTime(self):
        '''The timestamp when the virtual machine was most recently powered on.
        '''
        return self.data['bootTime']

    @property
    def cleanPowerOff(self):
        '''For a powered off virtual machine, indicates whether the virtual machine's last
        shutdown was an orderly power off or not. Unset if the virtual machine is
        running or suspended.
        '''
        return self.data['cleanPowerOff']

    @property
    def connectionState(self):
        '''Indicates whether or not the virtual machine is available for management.
        '''
        return self.data['connectionState']

    @property
    def device(self):
        '''Per-device runtime info. This array will be empty if the host software does not
        provide runtime info for any of the device types currently in use by the
        virtual machine.
        '''
        return self.data['device']

    @property
    def faultToleranceState(self):
        '''The fault tolerance state of the virtual machine.
        '''
        return self.data['faultToleranceState']

    @property
    def host(self):
        '''The host that is responsible for running a virtual machine. This property is null
        if the virtual machine is not running and is not assigned to run on a
        particular host.
        '''
        return self.data['host']

    @property
    def maxCpuUsage(self):
        '''Current upper-bound on CPU usage. The upper-bound is based on the host the virtual
        machine is current running on, as well as limits configured on the virtual
        machine itself or any parent resource pool. Valid while the virtual
        machine is running.
        '''
        return self.data['maxCpuUsage']

    @property
    def maxMemoryUsage(self):
        '''Current upper-bound on memory usage. The upper-bound is based on memory
        configuration of the virtual machine, as well as limits configured on the
        virtual machine itself or any parent resource pool. Valid while the
        virtual machine is running.
        '''
        return self.data['maxMemoryUsage']

    @property
    def memoryOverhead(self):
        '''The amount of memory resource (in bytes) that will be used by the virtual machine
        above its guest memory requirements. This value is set if and only if the
        virtual machine is registered on a host that supports memory resource
        allocation features.
        '''
        return self.data['memoryOverhead']

    @property
    def minRequiredEVCModeKey(self):
        '''For a powered-on or suspended virtual machine in a cluster with Enhanced VMotion
        Compatibility (EVC) enabled, this identifies the least-featured EVC mode
        (among those for the appropriate CPU vendor) that could admit the virtual
        machine. See EVCMode. This property will be unset if the virtual machine
        is powered off or is not in an EVC cluster.
        '''
        return self.data['minRequiredEVCModeKey']

    @property
    def needSecondaryReason(self):
        '''If set, indicates the reason the virtual machine needs a secondary.
        '''
        return self.data['needSecondaryReason']

    @property
    def numMksConnections(self):
        '''Number of active MKS connections to this virtual machine.
        '''
        return self.data['numMksConnections']

    @property
    def powerState(self):
        '''The current power state of the virtual machine.
        '''
        return self.data['powerState']

    @property
    def question(self):
        '''The current question, if any, that is blocking the virtual machine's execution.
        '''
        return self.data['question']

    @property
    def recordReplayState(self):
        '''Record / replay state of this virtual machine.
        '''
        return self.data['recordReplayState']

    @property
    def suspendInterval(self):
        '''The total time the virtual machine has been suspended since it was initially
        powered on. This time excludes the current period, if the virtual machine
        is currently suspended. This property is updated when the virtual machine
        resumes, and is reset to zero when the virtual machine is powered off.
        '''
        return self.data['suspendInterval']

    @property
    def suspendTime(self):
        '''The timestamp when the virtual machine was most recently suspended.
        '''
        return self.data['suspendTime']

    @property
    def toolsInstallerMounted(self):
        '''Flag to indicate whether or not the VMware Tools installer is mounted as a CD-ROM.
        '''
        return self.data['toolsInstallerMounted']

