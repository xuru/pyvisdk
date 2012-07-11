
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.managed_entity import ManagedEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachine(ManagedEntity):
    '''VirtualMachine is the managed object type for manipulating virtual machines,
    including templates that can be deployed (repeatedly) as new virtual machines.
    This type provides methods for configuring and controlling a virtual
    machine.VirtualMachine extends the ManagedEntity type because virtual machines
    are part of a virtual infrastructure inventory. The parent of a virtual machine
    must be a folder, and a virtual machine has no children.Destroying a virtual
    machine disposes of all associated storage, including the virtual disks. To
    remove a virtual machine while retaining its virtual disk storage, a client
    must remove the virtual disks from the virtual machine before destroying it.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.VirtualMachine):
        super(VirtualMachine, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def capability(self):
        '''Information about the runtime capabilities of this virtual machine.'''
        return self.update('capability')
    @property
    def config(self):
        '''Configuration of this virtual machine, including the name and UUID.'''
        return self.update('config')
    @property
    def datastore(self):
        '''A collection of references to the subset of datastore objects in the datacenter
        that is used by this virtual machine.'''
        return self.update('datastore')
    @property
    def environmentBrowser(self):
        '''The current virtual machine's environment browser object. This contains
        information on all the configurations that can be used on the virtual machine.
        This is identical to the environment browser on the ComputeResource to which
        this virtual machine belongs.'''
        return self.update('environmentBrowser')
    @property
    def guest(self):
        '''Information about VMware Tools and about the virtual machine from the
        perspective of VMware Tools. Information about the guest operating system is
        available in VirtualCenter. Guest operating system information reflects the
        last known state of the virtual machine. For powered on machines, this is
        current information. For powered off machines, this is the last recorded state
        before the virtual machine was powered off.'''
        return self.update('guest')
    @property
    def guestHeartbeatStatus(self):
        '''The guest heartbeat. The heartbeat status is classified as: * gray - VMware
        Tools are not installed or not running. * red - No heartbeat. Guest operating
        system may have stopped responding. * yellow - Intermittent heartbeat. May be
        due to guest load. * green - Guest operating system is responding normally. The
        guest heartbeat is a statistics metric. Alarms can be configured on this metric
        to trigger emails or other actions.'''
        return self.update('guestHeartbeatStatus')
    @property
    def layout(self):
        '''Detailed information about the files that comprise this virtual machine.'''
        return self.update('layout')
    @property
    def layoutEx(self):
        '''Detailed information about the files that comprise this virtual machine.'''
        return self.update('layoutEx')
    @property
    def network(self):
        '''A collection of references to the subset of network objects in the datacenter
        that is used by this virtual machine.'''
        return self.update('network')
    @property
    def parentVApp(self):
        '''Reference to the parent vApp.'''
        return self.update('parentVApp')
    @property
    def resourceConfig(self):
        '''The resource configuration for a virtual machine. The shares in this
        specification are evaluated relative to the resource pool to which it is
        assigned. This will return null if the product the virtual machine is
        registered on does not support resource configuration.'''
        return self.update('resourceConfig')
    @property
    def resourcePool(self):
        '''The current resource pool that specifies resource allocation for this virtual
        machine.'''
        return self.update('resourcePool')
    @property
    def rootSnapshot(self):
        '''The roots of all snapshot trees for the virtual machine.'''
        return self.update('rootSnapshot')
    @property
    def runtime(self):
        '''Execution state and history for this virtual machine.'''
        return self.update('runtime')
    @property
    def snapshot(self):
        '''Current snapshot and tree. The property is valid if snapshots have been created
        for this virtual machine.'''
        return self.update('snapshot')
    @property
    def storage(self):
        '''Storage space used by the virtual machine, split by datastore. Can be
        explicitly refreshed by the RefreshStorageInfo operation.'''
        return self.update('storage')
    @property
    def summary(self):
        '''Basic information about this virtual machine. This includes: * runtimeInfo *
        guest * basic configuration * alarms * performance information'''
        return self.update('summary')

    
    
    def AcquireMksTicket(self):
        '''<b>Deprecated.</b> <i>As of vSphere API 4.1, use AcquireTicket instead.</i>
        Creates and returns a one-time credential used in establishing a remote mouse-
        keyboard-screen connection to this virtual machine. The correct function of
        this method depends on being able to retrieve TCP binding information about the
        server end of the client connection that is requesting the ticket. If such
        information is not available, the NotSupported fault is thrown. This method is
        appropriate for SOAP and authenticated connections, which are both TCP-based
        connections.
        
        '''
        return self.delegate("AcquireMksTicket")()
    
    def AcquireTicket(self, ticketType):
        '''Creates and returns a one-time credential used in establishing a specific
        connection to this virtual machine, for example, a ticket type of mks can be
        used to establish a remote mouse-keyboard-screen connection.Creates and returns
        a one-time credential used in establishing a specific connection to this
        virtual machine, for example, a ticket type of mks can be used to establish a
        remote mouse-keyboard-screen connection.Creates and returns a one-time
        credential used in establishing a specific connection to this virtual machine,
        for example, a ticket type of mks can be used to establish a remote mouse-
        keyboard-screen connection.Creates and returns a one-time credential used in
        establishing a specific connection to this virtual machine, for example, a
        ticket type of mks can be used to establish a remote mouse-keyboard-screen
        connection.
        
        :param ticketType: The type of service to acquire, the set of possible values is described in VirtualMachineTicketType.
        
        '''
        return self.delegate("AcquireTicket")(ticketType)
    
    def AnswerVM(self, questionId, answerChoice):
        '''Responds to a question that is blocking this virtual machine.
        
        :param questionId: The value from QuestionInfo.id that identifies the question to answer.
        
        :param answerChoice: The contents of the QuestionInfo.choice.value array element that identifies the desired answer.
        
        '''
        return self.delegate("AnswerVM")(questionId, answerChoice)
    
    def CheckCustomizationSpec(self, spec):
        '''Checks the customization specification against the virtual machine
        configuration. For example, this is used on a source virtual machine before a
        clone operation to catch customization failure before the disk copy. This
        checks the specification's internal consistency as well as for compatibility
        with this virtual machine's configuration.
        
        :param spec: The customization specification to check.
        
        '''
        return self.delegate("CheckCustomizationSpec")(spec)
    
    def CloneVM_Task(self, folder, name, spec):
        '''Creates a clone of this virtual machine. If the virtual machine is used as a
        template, this method corresponds to the deploy command.Creates a clone of this
        virtual machine. If the virtual machine is used as a template, this method
        corresponds to the deploy command.Creates a clone of this virtual machine. If
        the virtual machine is used as a template, this method corresponds to the
        deploy command.Creates a clone of this virtual machine. If the virtual machine
        is used as a template, this method corresponds to the deploy command.Creates a
        clone of this virtual machine. If the virtual machine is used as a template,
        this method corresponds to the deploy command.Creates a clone of this virtual
        machine. If the virtual machine is used as a template, this method corresponds
        to the deploy command.
        
        :param folder: The location of the new virtual machine.
        
        :param name: The name of the new virtual machine.
        
        :param spec: Specifies how to clone the virtual machine.
        
        '''
        return self.delegate("CloneVM_Task")(folder, name, spec)
    
    def ConsolidateVMDisks_Task(self):
        '''Consolidate the virtual disk files of the virtual machine by finding
        hierarchies of redo logs that can be combined without violating data
        dependency. The redundant redo logs after merging are then deleted.
        Consolidation improves I/O performance since less number of virtual disk files
        need to be traversed; it also reduces the storage usage. However additional
        space is temporarily required to perform the operation. Use
        EstimateStorageForConsolidateSnapshots_Task to estimate the temporary space
        required. Consolidation can be I/O intensive, it is advisable to invoke this
        operation when guest is not under heavy I/O usage.
        
        '''
        return self.delegate("ConsolidateVMDisks_Task")()
    
    def CreateScreenshot_Task(self):
        '''Create a screen shot of a virtual machine.
        
        '''
        return self.delegate("CreateScreenshot_Task")()
    
    def CreateSecondaryVM_Task(self, host=None):
        '''Creates a secondary virtual machine to be part of this fault tolerant
        group.Creates a secondary virtual machine to be part of this fault tolerant
        group.Creates a secondary virtual machine to be part of this fault tolerant
        group.
        
        :param host: The host where the secondary virtual machine is to be created and powered on. If no host is specified, a compatible host will be selected by the system. If a host cannot be found for the secondary or the specified host is not suitable, the secondary will not be created and a fault will be returned.
        
        '''
        return self.delegate("CreateSecondaryVM_Task")(host)
    
    def CreateSnapshot_Task(self, name, memory, quiesce, description=None):
        '''Creates a new snapshot of this virtual machine. As a side effect, this updates
        the current snapshot.Creates a new snapshot of this virtual machine. As a side
        effect, this updates the current snapshot.Creates a new snapshot of this
        virtual machine. As a side effect, this updates the current snapshot.
        
        :param name: The name for this snapshot. The name need not be unique for this virtual machine.
        
        :param description: A description for this snapshot. If omitted, a default description may be provided.
        
        :param memory: If TRUE, a dump of the internal state of the virtual machine (basically a memory dump) is included in the snapshot. Memory snapshots consume time and resources, and thus take longer to create. When set to FALSE, the power state of the snapshot is set to powered off.
        
        :param quiesce: If TRUE and the virtual machine is powered on when the snapshot is taken, VMware Tools is used to quiesce the file system in the virtual machine. This assures that a disk snapshot represents a consistent state of the guest file systems. If the virtual machine is powered off or VMware Tools are not available, the quiesce flag is ignored.
        
        '''
        return self.delegate("CreateSnapshot_Task")(name, description, memory, quiesce)
    
    def CustomizeVM_Task(self, spec):
        '''Customizes a virtual machine's guest operating system.
        
        :param spec: The customization specification object.
        
        '''
        return self.delegate("CustomizeVM_Task")(spec)
    
    def DefragmentAllDisks(self):
        '''Defragment all virtual disks attached to this virtual machine.
        
        '''
        return self.delegate("DefragmentAllDisks")()
    
    def DisableSecondaryVM_Task(self, vm):
        '''Disables the specified secondary virtual machine in this fault tolerant group.
        The specified secondary will not be automatically started on a subsequent
        power-on of the primary virtual machine. This operation could leave the primary
        virtual machine in a non-fault tolerant state.
        
        :param vm: The secondary virtual machine specified will be disabed. This field must specify a secondary virtual machine that is part of the fault tolerant group that this virtual machine is currently associated with. It can only be invoked from the primary virtual machine in the group.
        
        '''
        return self.delegate("DisableSecondaryVM_Task")(vm)
    
    def EnableSecondaryVM_Task(self, vm, host=None):
        '''Enables the specified secondary virtual machine in this fault tolerant
        group.Enables the specified secondary virtual machine in this fault tolerant
        group.Enables the specified secondary virtual machine in this fault tolerant
        group.
        
        :param vm: The secondary virtual machine specified will be enabled. This field must specify a secondary virtual machine that is part of the fault tolerant group that this virtual machine is currently associated with. It can only be invoked from the primary virtual machine in the group.
        
        :param host: The host on which the secondary virtual machine is to be enabled and possibly powered on. If no host is specified, a compatible host will be selected by the system. If the secondary virtual machine is not compatible with the specified host, the secondary will not be re-enabled and a fault will be returned.
        
        '''
        return self.delegate("EnableSecondaryVM_Task")(vm, host)
    
    def EstimateStorageForConsolidateSnapshots_Task(self):
        '''Estimate the temporary space required to consolidation disk files. The
        estimation is a lower bound if the childmost writable disk file will be
        consolidated for an online virtual machine, it is accurate for all other
        situations. This is because the space requirement depending on the size of the
        childmost disk file and how write intensive the guest is.Estimate the temporary
        space required to consolidation disk files. The estimation is a lower bound if
        the childmost writable disk file will be consolidated for an online virtual
        machine, it is accurate for all other situations. This is because the space
        requirement depending on the size of the childmost disk file and how write
        intensive the guest is.
        
        '''
        return self.delegate("EstimateStorageForConsolidateSnapshots_Task")()
    
    def ExportVm(self):
        '''Obtains an export lease on this virtual machine. The export lease contains a
        list of URLs for the virtual disks for this virtual machine, as well as a
        ticket giving access to the URLs.Obtains an export lease on this virtual
        machine. The export lease contains a list of URLs for the virtual disks for
        this virtual machine, as well as a ticket giving access to the URLs.
        
        '''
        return self.delegate("ExportVm")()
    
    def ExtractOvfEnvironment(self):
        '''Returns the OVF environment for a virtual machine. If the virtual machine has
        no vApp configuration, an empty string is returned. Also, sensitive information
        is omitted, so this method is not guaranteed to return the complete OVF
        environment.
        
        '''
        return self.delegate("ExtractOvfEnvironment")()
    
    def MakePrimaryVM_Task(self, vm):
        '''Makes the specified secondary virtual machine from this fault tolerant group as
        the primary virtual machine.
        
        :param vm: The secondary virtual machine specified will be made the primary virtual machine. This field must specify a secondary virtual machine that is part of the fault tolerant group that this virtual machine is currently associated with. It can only be invoked from the primary virtual machine in the group.
        
        '''
        return self.delegate("MakePrimaryVM_Task")(vm)
    
    def MarkAsTemplate(self):
        '''Marks a VirtualMachine object as being used as a template. Note: A
        VirtualMachine marked as a template cannot be powered on.
        
        '''
        return self.delegate("MarkAsTemplate")()
    
    def MarkAsVirtualMachine(self, pool, host=None):
        '''Clears the 'isTemplate' flag and reassociates the virtual machine with a
        resource pool and host.
        
        :param pool: Resource pool to associate with the virtual machine.
        
        :param host: The target host on which the virtual machine is intended to run. The host parameter must specify a host that is a member of the ComputeResource indirectly specified by the pool. For a stand-alone host or a cluster with DRS, it can be omitted and the system selects a default.
        
        '''
        return self.delegate("MarkAsVirtualMachine")(pool, host)
    
    def MigrateVM_Task(self, priority, pool=None, host=None, state=None):
        '''Migrates a virtual machine's execution to a specific resource pool or
        host.Migrates a virtual machine's execution to a specific resource pool or
        host.
        
        :param pool: The target resource pool for the virtual machine. If the pool parameter is left unset, the virtual machine's current pool is used as the target pool.
        
        :param host: The target host to which the virtual machine is intended to migrate. The host parameter may be left unset if the compute resource associated with the target pool represents a stand-alone host or a DRS-enabled cluster. In the former case the stand-alone host is used as the target host. In the latter case, the DRS system selects an appropriate target host from the cluster.
        
        :param priority: The task priority (@see vim.VirtualMachine.MovePriority).
        
        :param state: If specified, the virtual machine migrates only if its state matches the specified state.
        
        '''
        return self.delegate("MigrateVM_Task")(pool, host, priority, state)
    
    def MountToolsInstaller(self):
        '''Mounts the VMware Tools CD installer as a CD-ROM for the guest operating
        system. To monitor the status of the tools install, clients should check the
        tools status, toolsVersionStatus and toolsRunningStatus
        
        '''
        return self.delegate("MountToolsInstaller")()
    
    def PowerOffVM_Task(self):
        '''Powers off this virtual machine. If this virtual machine is a fault tolerant
        primary virtual machine, this will result in the secondary virtual machine(s)
        getting powered off as well.
        
        '''
        return self.delegate("PowerOffVM_Task")()
    
    def PowerOnVM_Task(self, host=None):
        '''Powers on this virtual machine. If the virtual machine is suspended, this
        method resumes execution from the suspend point.Powers on this virtual machine.
        If the virtual machine is suspended, this method resumes execution from the
        suspend point.Powers on this virtual machine. If the virtual machine is
        suspended, this method resumes execution from the suspend point.
        
        :param host: (optional) The host where the virtual machine is to be powered on. If no host is specified, the current associated host is used. This field must specify a host that is part of the same compute resource that the virtual machine is currently associated with. If this host is not compatible, the current host association is used.
        
        '''
        return self.delegate("PowerOnVM_Task")(host)
    
    def PromoteDisks_Task(self, unlink, disks=None):
        '''Promotes disks on this virtual machine that have delta disk backings.Promotes
        disks on this virtual machine that have delta disk backings.Promotes disks on
        this virtual machine that have delta disk backings.
        
        :param unlink: If true, then these disks will be unlinked before consolidation.
        
        :param disks: The set of disks that are to be promoted. If this value is unset or the array is empty, all disks which have delta disk backings are promoted.
        
        '''
        return self.delegate("PromoteDisks_Task")(unlink, disks)
    
    def QueryChangedDiskAreas(self, deviceKey, startOffset, changeId, snapshot=None):
        '''Get a list of areas of a virtual disk belonging to this VM that have been
        modified since a well-defined point in the past. The beginning of the change
        interval is identified by "changeId", while the end of the change interval is
        implied by the snapshot ID passed in.Get a list of areas of a virtual disk
        belonging to this VM that have been modified since a well-defined point in the
        past. The beginning of the change interval is identified by "changeId", while
        the end of the change interval is implied by the snapshot ID passed in.
        
        :param snapshot: Snapshot for which changes that have been made sine "changeId" should be computed. If not set, changes are computed against the "current" snapshot of the virtual machine. However, using the "current" snapshot will only work for virtual machines that are powered off.
        
        :param deviceKey: Identifies the virtual disk for which to compute changes.
        
        :param startOffset: Start Offset in bytes at which to start computing changes. Typically, callers will make multiple calls to this function, starting with startOffset 0 and then examine the "length" property in the returned DiskChangeInfo structure, repeatedly calling queryChangedDiskAreas until a map forthe entire virtual disk has been obtained.
        
        :param changeId: Identifyer referring to a point in the past that should be used as the point in time at which to begin including changes to the disk in the result. A typical use case would be a backup application obtaining a changeId from a virtual disk's backing info when performing a backup. When a subsequent incremental backup is to be performed, this change Id can be used to obtain a list of changed areas on disk.
        
        '''
        return self.delegate("QueryChangedDiskAreas")(snapshot, deviceKey, startOffset, changeId)
    
    def QueryFaultToleranceCompatibility(self):
        '''This API can be invoked to determine whether a virtual machine is compatible
        for Fault Tolerance. The API only checks for VM-specific factors that impact
        compatibility for Fault Tolerance. Other requirements for Fault Tolerance such
        as host processor compatibility, logging nic configuration and licensing are
        not covered by this API. The query returns a list of faults, each fault
        corresponding to a specific incompatibility. If a given virtual machine is
        compatible for Fault Tolerance, then the fault list returned will be empty.
        
        '''
        return self.delegate("QueryFaultToleranceCompatibility")()
    
    def QueryUnownedFiles(self):
        '''For all files that belong to the vm, check that the file owner is set to the
        current datastore principal user, as set by
        HostDatastoreSystem.ConfigureDatastorePrincipal
        
        '''
        return self.delegate("QueryUnownedFiles")()
    
    def RebootGuest(self):
        '''Issues a command to the guest operating system asking it to perform a reboot.
        Returns immediately and does not wait for the guest operating system to
        complete the operation.
        
        '''
        return self.delegate("RebootGuest")()
    
    def ReconfigVM_Task(self, spec):
        '''Reconfigures this virtual machine. All the changes in the given configuration
        are applied to the virtual machine as an atomic operation.Reconfigures this
        virtual machine. All the changes in the given configuration are applied to the
        virtual machine as an atomic operation.Reconfigures this virtual machine. All
        the changes in the given configuration are applied to the virtual machine as an
        atomic operation.Reconfigures this virtual machine. All the changes in the
        given configuration are applied to the virtual machine as an atomic
        operation.Reconfigures this virtual machine. All the changes in the given
        configuration are applied to the virtual machine as an atomic
        operation.Reconfigures this virtual machine. All the changes in the given
        configuration are applied to the virtual machine as an atomic
        operation.Reconfigures this virtual machine. All the changes in the given
        configuration are applied to the virtual machine as an atomic operation.
        
        :param spec: The new configuration values.
        
        '''
        return self.delegate("ReconfigVM_Task")(spec)
    
    def RefreshStorageInfo(self):
        '''Explicitly refreshes the storage information of this virtual machine, updating
        properties storage, layoutEx and storage.
        
        '''
        return self.delegate("RefreshStorageInfo")()
    
    def reloadVirtualMachineFromPath_Task(self, configurationPath):
        '''Reloads the configuration for this virtual machine from a given datastore path.
        This is equivalent to unregistering and registering the virtual machine from a
        different path. The virtual machine's hardware configuration, snapshots,
        guestinfo variables etc. will be replaced based on the new configuration file.
        Other information associated with the virtual machine object, such as events
        and permissions, will be preserved.Reloads the configuration for this virtual
        machine from a given datastore path. This is equivalent to unregistering and
        registering the virtual machine from a different path. The virtual machine's
        hardware configuration, snapshots, guestinfo variables etc. will be replaced
        based on the new configuration file. Other information associated with the
        virtual machine object, such as events and permissions, will be
        preserved.Reloads the configuration for this virtual machine from a given
        datastore path. This is equivalent to unregistering and registering the virtual
        machine from a different path. The virtual machine's hardware configuration,
        snapshots, guestinfo variables etc. will be replaced based on the new
        configuration file. Other information associated with the virtual machine
        object, such as events and permissions, will be preserved.
        
        :param configurationPath: 
        
        '''
        return self.delegate("reloadVirtualMachineFromPath_Task")(configurationPath)
    
    def RelocateVM_Task(self, spec, priority=None):
        '''Relocates a virtual machine's virtual disks to a specific location; optionally
        moves the virtual machine to a different host as well.Relocates a virtual
        machine's virtual disks to a specific location; optionally moves the virtual
        machine to a different host as well.Relocates a virtual machine's virtual disks
        to a specific location; optionally moves the virtual machine to a different
        host as well.
        
        :param spec: The specification of where to relocate the virtual machine.
        
        :param priority: The task priority (@see vim.VirtualMachine.MovePriority).vSphere API 4.0
        
        '''
        return self.delegate("RelocateVM_Task")(spec, priority)
    
    def RemoveAllSnapshots_Task(self, consolidate=None):
        '''Remove all the snapshots associated with this virtual machine. If the virtual
        machine does not have any snapshots, then this operation simply returns
        successfully.
        
        :param consolidate: (optional) If set to true, the virtual disks of the deleted snapshot will be merged with other disk if possible. Default to true.vSphere API 5.0
        
        '''
        return self.delegate("RemoveAllSnapshots_Task")(consolidate)
    
    def ResetGuestInformation(self):
        '''Clears cached guest information. Guest information can be cleared only if the
        virtual machine is powered off.Clears cached guest information. Guest
        information can be cleared only if the virtual machine is powered off.
        
        '''
        return self.delegate("ResetGuestInformation")()
    
    def ResetVM_Task(self):
        '''Resets power on this virtual machine. If the current state is poweredOn, then
        this method first performs powerOff(hard). Once the power state is poweredOff,
        then this method performs powerOn(option).Resets power on this virtual machine.
        If the current state is poweredOn, then this method first performs
        powerOff(hard). Once the power state is poweredOff, then this method performs
        powerOn(option).
        
        '''
        return self.delegate("ResetVM_Task")()
    
    def RevertToCurrentSnapshot_Task(self, host=None, suppressPowerOn=None):
        '''Reverts the virtual machine to the current snapshot. This is equivalent to
        doing snapshot.currentSnapshot.revert.Reverts the virtual machine to the
        current snapshot. This is equivalent to doing snapshot.currentSnapshot.revert.
        
        :param host: (optional) Choice of host for the virtual machine, in case this operation causes the virtual machine to power on.
        
        :param suppressPowerOn: (optional) If set to true, the virtual machine will not be powered on regardless of the power state when the current snapshot was created. Default to false.vSphere API 4.0
        
        '''
        return self.delegate("RevertToCurrentSnapshot_Task")(host, suppressPowerOn)
    
    def SetDisplayTopology(self, displays):
        '''Sets the console window's display topology as specified.
        
        :param displays: The topology for each monitor that the virtual machine's display must span.
        
        '''
        return self.delegate("SetDisplayTopology")(displays)
    
    def SetScreenResolution(self, width, height):
        '''Sets the console window's resolution as specified.
        
        :param width: The screen width that should be set.
        
        :param height: The screen height that should be set.
        
        '''
        return self.delegate("SetScreenResolution")(width, height)
    
    def ShutdownGuest(self):
        '''Issues a command to the guest operating system asking it to perform a clean
        shutdown of all services. Returns immediately and does not wait for the guest
        operating system to complete the operation.
        
        '''
        return self.delegate("ShutdownGuest")()
    
    def StandbyGuest(self):
        '''Issues a command to the guest operating system asking it to prepare for a
        suspend operation. Returns immediately and does not wait for the guest
        operating system to complete the operation.
        
        '''
        return self.delegate("StandbyGuest")()
    
    def StartRecording_Task(self, name, description=None):
        '''Initiates a recording session on this virtual machine. As a side effect, this
        operation creates a snapshot on the virtual machine, which in turn becomes the
        current snapshot.Initiates a recording session on this virtual machine. As a
        side effect, this operation creates a snapshot on the virtual machine, which in
        turn becomes the current snapshot.
        
        :param name: The name for the snapshot associated with this recording. The name need not be unique for this virtual machine.
        
        :param description: A description for the snapshot associated with this recording. If omitted, a default description may be provided.
        
        '''
        return self.delegate("StartRecording_Task")(name, description)
    
    def StartReplaying_Task(self, replaySnapshot):
        '''Starts a replay session on this virtual machine. As a side effect, this
        operation updates the current snapshot of the virtual machine.Starts a replay
        session on this virtual machine. As a side effect, this operation updates the
        current snapshot of the virtual machine.
        
        :param replaySnapshot: The snapshot from which to start the replay. This snapshot must have been created by a record operation on the virtual machine.
        
        '''
        return self.delegate("StartReplaying_Task")(replaySnapshot)
    
    def StopRecording_Task(self):
        '''Stops a currently active recording session on this virtual machine.Stops a
        currently active recording session on this virtual machine.
        
        '''
        return self.delegate("StopRecording_Task")()
    
    def StopReplaying_Task(self):
        '''Stops a replay session on this virtual machine.Stops a replay session on this
        virtual machine.
        
        '''
        return self.delegate("StopReplaying_Task")()
    
    def SuspendVM_Task(self):
        '''Suspends execution in this virtual machine.
        
        '''
        return self.delegate("SuspendVM_Task")()
    
    def TerminateFaultTolerantVM_Task(self, vm=None):
        '''Terminates the specified secondary virtual machine in a fault tolerant group.
        This can be used to test fault tolerance on a given virtual machine, and should
        be used with care.
        
        :param vm: The secondary virtual machine specified will be terminated, allowing fault tolerance to activate. If no virtual machine is specified, all secondary virtual machines will be terminated. If vm is a primary, InvalidArgument exception is thrown. This field must specify a virtual machine that is part of the fault tolerant group that this virtual machine is currently associated with. It can only be invoked from the primary virtual machine in the group. If the primary virtual machine is terminated, an available secondary virtual machine will be promoted to primary. If no secondary exists, an exception will be thrown and the primary virtual machine will not be terminated. If a secondary virtual machine is terminated, it may be respawned on a potentially different host.
        
        '''
        return self.delegate("TerminateFaultTolerantVM_Task")(vm)
    
    def TurnOffFaultToleranceForVM_Task(self):
        '''Removes all secondary virtual machines associated with the fault tolerant group
        and turns off protection for this virtual machine. This operation can only be
        invoked from the primary virtual machine in the group.
        
        '''
        return self.delegate("TurnOffFaultToleranceForVM_Task")()
    
    def UnmountToolsInstaller(self):
        '''Unmounts VMware Tools installer CD.
        
        '''
        return self.delegate("UnmountToolsInstaller")()
    
    def UnregisterVM(self):
        '''Removes this virtual machine from the inventory without removing any of the
        virtual machine's files on disk. All high-level information stored with the
        management server (ESX Server or VirtualCenter) is removed, including
        information such as statistics, resource pool association, permissions, and
        alarms.Removes this virtual machine from the inventory without removing any of
        the virtual machine's files on disk. All high-level information stored with the
        management server (ESX Server or VirtualCenter) is removed, including
        information such as statistics, resource pool association, permissions, and
        alarms.
        
        '''
        return self.delegate("UnregisterVM")()
    
    def UpgradeTools_Task(self, installerOptions=None):
        '''Begins the tools upgrade process. To monitor the status of the tools install,
        clients should check the tools status, toolsVersionStatus and
        toolsRunningStatus.
        
        :param installerOptions: Command line options passed to the installer to modify the installation procedure for tools.
        
        '''
        return self.delegate("UpgradeTools_Task")(installerOptions)
    
    def UpgradeVM_Task(self, version=None):
        '''Upgrades this virtual machine's virtual hardware to the latest revision that is
        supported by the virtual machine's current host.
        
        :param version: If specified, upgrade to that specified version. If not specified, upgrade to the most current virtual hardware supported on the host.
        
        '''
        return self.delegate("UpgradeVM_Task")(version)