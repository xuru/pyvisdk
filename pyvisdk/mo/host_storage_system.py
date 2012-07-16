
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostStorageSystem(ExtensibleManagedObject):
    '''This managed object gets and sets configuration information about the host's
    storage subsystem. The properties and operations are used to configure the host
    to make storage available for virtual machines. This object contains properties
    that are specific to ESX Server and general to both the ESX Server system and
    the hosted architecture.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostStorageSystem):
        super(HostStorageSystem, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def fileSystemVolumeInfo(self):
        '''File system volume information for the host. See the FileSystemVolumeInfo data
        object type for more information.'''
        return self.update('fileSystemVolumeInfo')
    @property
    def multipathStateInfo(self):
        '''Runtime information about the state of a multipath path. A null value will be
        returned if path state information is not available for this system.'''
        return self.update('multipathStateInfo')
    @property
    def storageDeviceInfo(self):
        '''Host storage information up to the device level.'''
        return self.update('storageDeviceInfo')
    @property
    def systemFile(self):
        '''Datastore paths of files used by the host system on mounted volumes, for
        instance, the COS vmdk file of the host. For information on datastore paths,
        see Datastore.'''
        return self.update('systemFile')

    
    
    def AddInternetScsiSendTargets(self, iScsiHbaDevice, targets):
        '''Adds Send Target entries to the host bus adapter discovery list. The
        DiscoveryProperties.sendTargetsDiscoveryEnabled flag must be set to true.
        
        :param iScsiHbaDevice: The device of the Internet SCSI HBA adapter.
        
        :param targets: An array of iSCSI send targets.
        
        '''
        return self.delegate("AddInternetScsiSendTargets")(iScsiHbaDevice, targets)
    
    def AddInternetScsiStaticTargets(self, iScsiHbaDevice, targets):
        '''Adds Static Target entries to the host bus adapter discovery list. The
        DiscoveryProperty.staticTargetDiscoveryEnabled must be set to true.
        
        :param iScsiHbaDevice: The device of the Internet SCSI HBA adapter.
        
        :param targets: An array of iSCSI static targets to add.
        
        '''
        return self.delegate("AddInternetScsiStaticTargets")(iScsiHbaDevice, targets)
    
    def AttachScsiLun(self, lunUuid):
        '''Allow I/O issue to the specified detached ScsiLun. The ScsiLun is
        administratively configured on, if the attach operation is successful. See
        DetachScsiLun.Allow I/O issue to the specified detached ScsiLun. The ScsiLun is
        administratively configured on, if the attach operation is successful. See
        DetachScsiLun.
        
        :param lunUuid: The uuid of the ScsiLun to update.
        
        '''
        return self.delegate("AttachScsiLun")(lunUuid)
    
    def AttachVmfsExtent(self, vmfsPath, extent):
        '''Extends a VMFS by attaching a disk partition as an extent.
        
        :param vmfsPath: The path of the VMFS to extend. See FileSystemMountInfo.
        
        :param extent: A data object that describes the specification of a Disk partition.
        
        '''
        return self.delegate("AttachVmfsExtent")(vmfsPath, extent)
    
    def ComputeDiskPartitionInfo(self, devicePath, layout, partitionFormat=None):
        '''Computes the disk partition information given the desired disk layout. The
        server computes a new partition information object for a specific disk
        representing the desired layout.See HostDiskPartitionInfoPartitionFormat
        
        :param devicePath: The name of the device path for the specific disk.See HostDiskPartitionInfoPartitionFormat
        
        :param layout: A data object that describes the disk partition layout.See HostDiskPartitionInfoPartitionFormat
        
        :param partitionFormat: Specifies the desired partition format to be computed from the block range. If partitionFormat is not specified, the existing partitionFormat on disk is used, if the disk is not blank and mbr otherwise.See HostDiskPartitionInfoPartitionFormatvSphere API 5.0
        
        '''
        return self.delegate("ComputeDiskPartitionInfo")(devicePath, layout, partitionFormat)
    
    def ComputeDiskPartitionInfoForResize(self, partition, blockRange, partitionFormat=None):
        '''Computes the disk partition information for the purpose of resizing a given
        partition.See HostDiskPartitionInfoPartitionFormat
        
        :param partition: The disk partition to resize.See HostDiskPartitionInfoPartitionFormat
        
        :param blockRange: Specifies the desired block range for the resized partition. The start of the block range specified should match that of the current partition.See HostDiskPartitionInfoPartitionFormat
        
        :param partitionFormat: Specifies the desired partition format to be computed from the block range. If partitionFormat is not specified, the existing partitionFormat on disk is used, if the disk is not blank and mbr otherwise.See HostDiskPartitionInfoPartitionFormatvSphere API 5.0
        
        '''
        return self.delegate("ComputeDiskPartitionInfoForResize")(partition, blockRange, partitionFormat)
    
    def DetachScsiLun(self, lunUuid):
        '''Disallow I/O issue to the specified ScsiLun. The ScsiLun is detached, i.e.
        administratively configured off until a subsequent attachScsiLun is performed,
        if the operation is successful. See AttachScsiLun.Disallow I/O issue to the
        specified ScsiLun. The ScsiLun is detached, i.e. administratively configured
        off until a subsequent attachScsiLun is performed, if the operation is
        successful. See AttachScsiLun.
        
        :param lunUuid: The uuid of the ScsiLun device to detach.
        
        '''
        return self.delegate("DetachScsiLun")(lunUuid)
    
    def DisableMultipathPath(self, pathName):
        '''Disables an enabled path for a Logical Unit. Use the path name from
        HostMultipathStateInfoPath or HostMultipathInfoPath.
        
        :param pathName: The name of the path to disable.
        
        '''
        return self.delegate("DisableMultipathPath")(pathName)
    
    def DiscoverFcoeHbas(self, fcoeSpec):
        '''Initiates FCoE discovery using the given FcoeSpecification. Upon success,
        discovered VNPorts will have registered with the system as FCoE HBAs.
        
        :param fcoeSpec: 
        
        '''
        return self.delegate("DiscoverFcoeHbas")(fcoeSpec)
    
    def EnableMultipathPath(self, pathName):
        '''Enables a disabled path for a Logical Unit. Use the path name from
        HostMultipathStateInfoPath or HostMultipathInfoPath.
        
        :param pathName: The name of the path to enable.
        
        '''
        return self.delegate("EnableMultipathPath")(pathName)
    
    def ExpandVmfsExtent(self, vmfsPath, extent):
        '''Expands a VMFS extent as specified by the Disk partition specification.
        
        :param vmfsPath: The path of the VMFS to expand. See FileSystemMountInfo.
        
        :param extent: The disk partition corresponding to the extent to be expanded.
        
        '''
        return self.delegate("ExpandVmfsExtent")(vmfsPath, extent)
    
    def FormatVmfs(self, createSpec):
        '''Formats a new VMFS on a disk partition.
        
        :param createSpec: A data object that describes the VMware File System (VMFS) creation specification.
        
        '''
        return self.delegate("FormatVmfs")(createSpec)
    
    def MarkForRemoval(self, hbaName, remove):
        '''Mark or unmark the given FCoE HBA for removal from the host system. Marking an
        FCoE HBA for removal will result in the HBA not being discovered upon host
        reboot. Until reboot, the HBA remains visible in the storage topology.
        
        :param hbaName: 
        
        :param remove: 
        
        '''
        return self.delegate("MarkForRemoval")(hbaName, remove)
    
    def MountVmfsVolume(self, vmfsUuid):
        '''Mount the unmounted Vmfs volume. A newly discovered vmfs volume will be mounted
        unless, it has been explicitly unmounted. The default mount behavior of Vmfs
        volumes is auto-mount. See UnmountVmfsVolume.Mount the unmounted Vmfs volume. A
        newly discovered vmfs volume will be mounted unless, it has been explicitly
        unmounted. The default mount behavior of Vmfs volumes is auto-mount. See
        UnmountVmfsVolume.
        
        :param vmfsUuid: 
        
        '''
        return self.delegate("MountVmfsVolume")(vmfsUuid)
    
    def QueryPathSelectionPolicyOptions(self):
        '''Queries the set of path selection policy options. The set of policy options
        indicates what path selection policies can be used by a device managed by
        native multipathing. Devices managed through native multipathing are described
        in the HostMultipathInfo data object.Queries the set of path selection policy
        options. The set of policy options indicates what path selection policies can
        be used by a device managed by native multipathing. Devices managed through
        native multipathing are described in the HostMultipathInfo data object.
        
        '''
        return self.delegate("QueryPathSelectionPolicyOptions")()
    
    def QueryStorageArrayTypePolicyOptions(self):
        '''Queries the set of storage array type policy options. The set of policy options
        indicates what storage array type policies can be used by a device managed by
        native multipathing. Devices managed through native multipathing are described
        in the HostMultipathInfo data object.Queries the set of storage array type
        policy options. The set of policy options indicates what storage array type
        policies can be used by a device managed by native multipathing. Devices
        managed through native multipathing are described in the HostMultipathInfo data
        object.
        
        '''
        return self.delegate("QueryStorageArrayTypePolicyOptions")()
    
    def QueryUnresolvedVmfsVolume(self):
        '''Get the list of unbound VMFS volumes. For sharing a volume across hosts, a VMFS
        volume is bound to its underlying block device storage. When a low level block
        copy is performed to copy or move the VMFS volume, the copied volume will be
        unbound.
        
        '''
        return self.delegate("QueryUnresolvedVmfsVolume")()
    
    def RefreshStorageSystem(self):
        '''Obtains the latest host storage information related to storage devices,
        topology, and file systems. The ESX host updates its storage information
        asynchronously. The RefreshStorageSystem method obtains information from the
        host platform and it performs a rescan of VMFS volumes. It does not look for
        new devices.Obtains the latest host storage information related to storage
        devices, topology, and file systems. The ESX host updates its storage
        information asynchronously. The RefreshStorageSystem method obtains information
        from the host platform and it performs a rescan of VMFS volumes. It does not
        look for new devices.Obtains the latest host storage information related to
        storage devices, topology, and file systems. The ESX host updates its storage
        information asynchronously. The RefreshStorageSystem method obtains information
        from the host platform and it performs a rescan of VMFS volumes. It does not
        look for new devices.Obtains the latest host storage information related to
        storage devices, topology, and file systems. The ESX host updates its storage
        information asynchronously. The RefreshStorageSystem method obtains information
        from the host platform and it performs a rescan of VMFS volumes. It does not
        look for new devices.
        
        '''
        return self.delegate("RefreshStorageSystem")()
    
    def RemoveInternetScsiSendTargets(self, iScsiHbaDevice, targets):
        '''Removes Send Target entries from the host bus adapter discovery list. The
        DiscoveryProperty.sendTargetsDiscoveryEnabled must be set to true. If any of
        the targets provided as parameters are not found in the existing list, the
        other targets are removed and an exception is thrown.
        
        :param iScsiHbaDevice: The device of the Internet SCSI HBA adapter.
        
        :param targets: An array of iSCSI send targets to remove.
        
        '''
        return self.delegate("RemoveInternetScsiSendTargets")(iScsiHbaDevice, targets)
    
    def RemoveInternetScsiStaticTargets(self, iScsiHbaDevice, targets):
        '''Removes static target entries from the host bus adapter discovery list. The
        DiscoveryProperty.staticTargetDiscoveryEnabled must be set to true. If any of
        the targets provided as parameters are not found in the existing list, the
        other targets are removed and an exception is thrown.
        
        :param iScsiHbaDevice: The device of the Internet SCSI HBA adapter.
        
        :param targets: An array of iSCSI static targets to remove.
        
        '''
        return self.delegate("RemoveInternetScsiStaticTargets")(iScsiHbaDevice, targets)
    
    def RescanAllHba(self):
        '''Scans all host bus adapters to obtain the current list of devices and device
        topology. The RescanAllHba method looks for new devices, removed devices, and
        path changes.Scans all host bus adapters to obtain the current list of devices
        and device topology. The RescanAllHba method looks for new devices, removed
        devices, and path changes.Scans all host bus adapters to obtain the current
        list of devices and device topology. The RescanAllHba method looks for new
        devices, removed devices, and path changes.Scans all host bus adapters to
        obtain the current list of devices and device topology. The RescanAllHba method
        looks for new devices, removed devices, and path changes.
        
        '''
        return self.delegate("RescanAllHba")()
    
    def RescanHba(self, hbaDevice):
        '''Issues a request to rescan a specific host bus adapter for new storage devices.
        
        :param hbaDevice: The device of the host bus adapter.
        
        '''
        return self.delegate("RescanHba")(hbaDevice)
    
    def RescanVmfs(self):
        '''Rescans for new Virtual Machine File Systems (VMFS). The RefreshStorageSystem
        method also performs a VMFS rescan.Rescans for new Virtual Machine File Systems
        (VMFS). The RefreshStorageSystem method also performs a VMFS rescan.
        
        '''
        return self.delegate("RescanVmfs")()
    
    def ResolveMultipleUnresolvedVmfsVolumes(self, resolutionSpec):
        '''Resignature or 'Force Mount' list of unbound VMFS volumes. To safely enable
        sharing of the volume across hosts, a VMFS volume is bound to its underlying
        block device storage. When a low level block copy is performed to copy or move
        the VMFS volume, the copied volume will be unbound. In order for the VMFS
        volume to be usable, a resolution operation is needed to determine whether the
        VMFS volume should be treated as a new volume or not and what extents compose
        that volume in the event there is more than one unbound volume.Resignature or
        'Force Mount' list of unbound VMFS volumes. To safely enable sharing of the
        volume across hosts, a VMFS volume is bound to its underlying block device
        storage. When a low level block copy is performed to copy or move the VMFS
        volume, the copied volume will be unbound. In order for the VMFS volume to be
        usable, a resolution operation is needed to determine whether the VMFS volume
        should be treated as a new volume or not and what extents compose that volume
        in the event there is more than one unbound volume.Resignature or 'Force Mount'
        list of unbound VMFS volumes. To safely enable sharing of the volume across
        hosts, a VMFS volume is bound to its underlying block device storage. When a
        low level block copy is performed to copy or move the VMFS volume, the copied
        volume will be unbound. In order for the VMFS volume to be usable, a resolution
        operation is needed to determine whether the VMFS volume should be treated as a
        new volume or not and what extents compose that volume in the event there is
        more than one unbound volume.
        
        :param resolutionSpec: List of data object that describes what the disk extents to be used for creating the new VMFS volume.
        
        '''
        return self.delegate("ResolveMultipleUnresolvedVmfsVolumes")(resolutionSpec)
    
    def RetrieveDiskPartitionInfo(self, devicePath):
        '''Gets the partition information for the disks named by the device names.
        
        :param devicePath: An array of device path names that identify disks. See ScsiDisk.
        
        '''
        return self.delegate("RetrieveDiskPartitionInfo")(devicePath)
    
    def SetMultipathLunPolicy(self, lunId, policy):
        '''Updates the path selection policy for a Logical Unit. Use the LUN uuid from
        HostMultipathInfoLogicalUnit.
        
        :param lunId: The logical unit ID
        
        :param policy: A data object that describes a path selection policy for the logical unit.
        
        '''
        return self.delegate("SetMultipathLunPolicy")(lunId, policy)
    
    def UnmountForceMountedVmfsVolume(self, vmfsUuid):
        '''Unmount the 'forceMounted' Vmfs volume. When a low level block copy is
        performed to copy or move the VMFS volume, the copied volume is unresolved. For
        the VMFS volume to be usable, a resolution operation is applied. As part of
        resolution operation, user may decide to keep the original VMFS Uuid. Once the
        resolution is applied, the VMFS volume is mounted on the host for its use. User
        can unmount the VMFS volume if it is not being used by any registered VMs.
        
        :param vmfsUuid: 
        
        '''
        return self.delegate("UnmountForceMountedVmfsVolume")(vmfsUuid)
    
    def UnmountVmfsVolume(self, vmfsUuid):
        '''Unmount the Vmfs volume. An unmounted volume cannot be used for any filesystem
        operation requiring I/O. In contrast to removal, this operation does not
        destroy or alter partitions on which vmfs volumes reside. The mountState will
        be persisted across filesystem rescans and host reboots. See
        MountVmfsVolume.Unmount the Vmfs volume. An unmounted volume cannot be used for
        any filesystem operation requiring I/O. In contrast to removal, this operation
        does not destroy or alter partitions on which vmfs volumes reside. The
        mountState will be persisted across filesystem rescans and host reboots. See
        MountVmfsVolume.
        
        :param vmfsUuid: 
        
        '''
        return self.delegate("UnmountVmfsVolume")(vmfsUuid)
    
    def UpdateDiskPartitions(self, devicePath, spec):
        '''Changes the partitions on the disk by supplying a partition specification and
        the device name.
        
        :param devicePath: The name of the device path for the specific disk.
        
        :param spec: A data object that describes the disk partition table specification used to configure the partitions on a disk.
        
        '''
        return self.delegate("UpdateDiskPartitions")(devicePath, spec)
    
    def UpdateInternetScsiAdvancedOptions(self, iScsiHbaDevice, options, targetSet=None):
        '''Updates the advanced options the iSCSI host bus adapter or the discovery
        addresses and targets associated with it.
        
        :param iScsiHbaDevice: The device of the Internet SCSI HBA adapter.
        
        :param targetSet: The set the targets to configure. If not provided, the settings will be applied to the host bus adapter itself.
        
        :param options: The list of options to set.
        
        '''
        return self.delegate("UpdateInternetScsiAdvancedOptions")(iScsiHbaDevice, targetSet, options)
    
    def UpdateInternetScsiAlias(self, iScsiHbaDevice, iScsiAlias):
        '''Updates the alias of an iSCSI host bus adapter.
        
        :param iScsiHbaDevice: The device of the Internet SCSI HBA adapter.
        
        :param iScsiAlias: The new value for the alias of the adapter.
        
        '''
        return self.delegate("UpdateInternetScsiAlias")(iScsiHbaDevice, iScsiAlias)
    
    def UpdateInternetScsiAuthenticationProperties(self, iScsiHbaDevice, authenticationProperties, targetSet=None):
        '''Updates the authentication properties for one or more targets or discovery
        addresses associated with an iSCSI host bus adapter.
        
        :param iScsiHbaDevice: The device of the Internet SCSI HBA adapter. associated with the target.
        
        :param authenticationProperties: The data object that represents the authentication settings to set.
        
        :param targetSet: The set the targets to configure. Optional, when obmitted will configura the authentication properties for the adapter instead.vSphere API 4.0
        
        '''
        return self.delegate("UpdateInternetScsiAuthenticationProperties")(iScsiHbaDevice, authenticationProperties, targetSet)
    
    def UpdateInternetScsiDigestProperties(self, iScsiHbaDevice, digestProperties, targetSet=None):
        '''Updates the digest properties for the iSCSI host bus adapter or the discovery
        addresses and targets associated with it.
        
        :param iScsiHbaDevice: The device of the Internet SCSI HBA adapter.
        
        :param targetSet: The set the targets to configure. If not provided, the settings will be applied to the host bus adapter itself.
        
        :param digestProperties: The data object that represents the digest settings to set.
        
        '''
        return self.delegate("UpdateInternetScsiDigestProperties")(iScsiHbaDevice, targetSet, digestProperties)
    
    def UpdateInternetScsiDiscoveryProperties(self, iScsiHbaDevice, discoveryProperties):
        '''Updates the Discovery properties for an iSCSI host bus adapter.
        
        :param iScsiHbaDevice: The device of the Internet SCSI HBA adapter.
        
        :param discoveryProperties: The discovery settings for this host bus adapter.
        
        '''
        return self.delegate("UpdateInternetScsiDiscoveryProperties")(iScsiHbaDevice, discoveryProperties)
    
    def UpdateInternetScsiIPProperties(self, iScsiHbaDevice, ipProperties):
        '''Updates the IP properties for an iSCSI host bus adapter.
        
        :param iScsiHbaDevice: The device of the Internet SCSI HBA adapter.
        
        :param ipProperties: A data object representing the IP properties for the host bus adapter
        
        '''
        return self.delegate("UpdateInternetScsiIPProperties")(iScsiHbaDevice, ipProperties)
    
    def UpdateInternetScsiName(self, iScsiHbaDevice, iScsiName):
        '''Updates the name of an iSCSI host bus adapter.
        
        :param iScsiHbaDevice: The current name of the Internet SCSI HBA adapter.
        
        :param iScsiName: The new name for the Internet SCSI HBA adapter
        
        '''
        return self.delegate("UpdateInternetScsiName")(iScsiHbaDevice, iScsiName)
    
    def UpdateScsiLunDisplayName(self, lunUuid, displayName):
        '''Update the mutable display name associated with a ScsiLun. The ScsiLun to be
        updated is identified using the specified uuid.
        
        :param lunUuid: The uuid of the ScsiLun to update.
        
        :param displayName: The new name to assign to the ScsiLun object.
        
        '''
        return self.delegate("UpdateScsiLunDisplayName")(lunUuid, displayName)
    
    def UpdateSoftwareInternetScsiEnabled(self, enabled):
        '''Enables or disables Software iSCSI.
        
        :param enabled: True to enable the iSCSI; false to disable it
        
        '''
        return self.delegate("UpdateSoftwareInternetScsiEnabled")(enabled)
    
    def UpgradeVmfs(self, vmfsPath):
        '''Upgrades the VMFS to the latest supported VMFS version.Upgrades the VMFS to the
        latest supported VMFS version.
        
        :param vmfsPath: The path of the VMFS.
        
        '''
        return self.delegate("UpgradeVmfs")(vmfsPath)
    
    def UpgradeVmLayout(self):
        '''Iterates over all registered virtual machines. For each VM which .vmx file is
        located on the service console and all disks are available on VMFS3 or NAS, it
        will relocate the disks into directories if stored in the ROOT, and relocate
        the VMX file into the directory too. Events are logged for each virtual machine
        that is relocated.Iterates over all registered virtual machines. For each VM
        which .vmx file is located on the service console and all disks are available
        on VMFS3 or NAS, it will relocate the disks into directories if stored in the
        ROOT, and relocate the VMX file into the directory too. Events are logged for
        each virtual machine that is relocated.
        
        '''
        return self.delegate("UpgradeVmLayout")()