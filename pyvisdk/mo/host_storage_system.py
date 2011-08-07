
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostStorageSystem(ExtensibleManagedObject):
    '''This managed object gets and sets configuration information about the host's
        storage subsystem. The properties and operations are used to configure the
        host to make storage available for virtual machines. This object contains
        properties that are specific to ESX Server and general to both the ESX
        Server system and the hosted architecture.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostStorageSystem):
        # MUST define these
        super(HostStorageSystem, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def fileSystemVolumeInfo(self):
        '''File system volume information for the host. See the FileSystemVolumeInfo data
        object type for more information.
        '''
        return self.update('fileSystemVolumeInfo')

    @property
    def multipathStateInfo(self):
        '''Runtime information about the state of a multipath path. A null value will be
        returned if path state information is not available for this system.
        '''
        return self.update('multipathStateInfo')

    @property
    def storageDeviceInfo(self):
        '''Host storage information up to the device level.
        '''
        return self.update('storageDeviceInfo')

    @property
    def systemFile(self):
        '''Datastore paths of files used by the host system on mounted volumes, for instance,
        the COS vmdk file of the host. For information on datastore paths, see
        Datastore.
        '''
        return self.update('systemFile')


    def AddInternetScsiSendTargets(self):
        '''Adds Send Target entries to the host bus adapter discovery list. The
        DiscoveryProperties.sendTargetsDiscoveryEnabled flag must be set to true.
        '''
        
        return self.delegate("AddInternetScsiSendTargets")()
        

    def AddInternetScsiStaticTargets(self):
        '''Adds Static Target entries to the host bus adapter discovery list. The
        DiscoveryProperty.staticTargetDiscoveryEnabled must be set to true.
        '''
        
        return self.delegate("AddInternetScsiStaticTargets")()
        

    def AttachVmfsExtent(self):
        '''Extends a VMFS by attaching a disk partition as an extent.
        '''
        
        return self.delegate("AttachVmfsExtent")()
        

    def ComputeDiskPartitionInfo(self):
        '''Computes the disk partition information given the desired disk layout. The server
        computes a new partition information object for a specific disk
        representing the desired layout. See HostDiskPartitionInfoPartitionFormat
        '''
        
        return self.delegate("ComputeDiskPartitionInfo")()
        

    def ComputeDiskPartitionInfoForResize(self):
        '''Computes the disk partition information for the purpose of resizing a given
        partition. See HostDiskPartitionInfoPartitionFormat
        '''
        
        return self.delegate("ComputeDiskPartitionInfoForResize")()
        

    def DisableMultipathPath(self):
        '''Disables an enabled path for a Logical Unit. Use the path name from
        HostMultipathStateInfoPath or HostMultipathInfoPath.
        '''
        
        return self.delegate("DisableMultipathPath")()
        

    def EnableMultipathPath(self):
        '''Enables a disabled path for a Logical Unit. Use the path name from
        HostMultipathStateInfoPath or HostMultipathInfoPath.
        '''
        
        return self.delegate("EnableMultipathPath")()
        

    def ExpandVmfsExtent(self):
        '''Expands a VMFS extent as specified by the Disk partition specification.
        '''
        
        return self.delegate("ExpandVmfsExtent")()
        

    def FormatVmfs(self):
        '''Formats a new VMFS on a disk partition.
        '''
        
        return self.delegate("FormatVmfs")()
        

    def QueryPathSelectionPolicyOptions(self):
        '''Queries the set of path selection policy options. The set of policy options
        indicates what path selection policies can be used by a device managed by
        native multipathing. Devices managed through native multipathing are
        described in the HostMultipathInfo data object.Filtering capabilities are
        not currently present but may be added in the future.
        '''
        
        return self.delegate("QueryPathSelectionPolicyOptions")()
        

    def QueryStorageArrayTypePolicyOptions(self):
        '''Queries the set of storage array type policy options. The set of policy options
        indicates what storage array type policies can be used by a device managed
        by native multipathing. Devices managed through native multipathing are
        described in the HostMultipathInfo data object.Filtering capabilities are
        not currently present but may be added in the future.
        '''
        
        return self.delegate("QueryStorageArrayTypePolicyOptions")()
        

    def QueryUnresolvedVmfsVolume(self):
        '''Get the list of unbound VMFS volumes. For sharing a volume across hosts, a VMFS
        volume is bound to its underlying block device storage. When a low level
        block copy is performed to copy or move the VMFS volume, the copied volume
        will be unbound.
        '''
        
        return self.delegate("QueryUnresolvedVmfsVolume")()
        

    def RefreshStorageSystem(self):
        '''Refresh the storage information and settings to pick up any changes that might
        have occurred.
        '''
        
        return self.delegate("RefreshStorageSystem")()
        

    def RemoveInternetScsiSendTargets(self):
        '''Removes Send Target entries from the host bus adapter discovery list. The
        DiscoveryProperty.sendTargetsDiscoveryEnabled must be set to true. If any
        of the targets provided as parameters are not found in the existing list,
        the other targets are removed and an exception is thrown.
        '''
        
        return self.delegate("RemoveInternetScsiSendTargets")()
        

    def RemoveInternetScsiStaticTargets(self):
        '''Removes static target entries from the host bus adapter discovery list. The
        DiscoveryProperty.staticTargetDiscoveryEnabled must be set to true. If any
        of the targets provided as parameters are not found in the existing list,
        the other targets are removed and an exception is thrown.
        '''
        
        return self.delegate("RemoveInternetScsiStaticTargets")()
        

    def RescanAllHba(self):
        '''Issues a request to rescan all host bus adapters for new storage devices.
        '''
        
        return self.delegate("RescanAllHba")()
        

    def RescanHba(self):
        '''Issues a request to rescan a specific host bus adapter for new storage devices.
        '''
        
        return self.delegate("RescanHba")()
        

    def RescanVmfs(self):
        '''Rescans for new VMFSs that might have been added.
        '''
        
        return self.delegate("RescanVmfs")()
        

    def ResolveMultipleUnresolvedVmfsVolumes(self):
        '''Resignature or 'Force Mount' list of unbound VMFS volumes. To safely enable
        sharing of the volume across hosts, a VMFS volume is bound to its
        underlying block device storage. When a low level block copy is performed
        to copy or move the VMFS volume, the copied volume will be unbound. In
        order for the VMFS volume to be usable, a resolution operation is needed
        to determine whether the VMFS volume should be treated as a new volume or
        not and what extents compose that volume in the event there is more than
        one unbound volume.Resignature results in a new VMFS volume on the host.
        Operations performed at the StorageSystem interface apply only to a
        specific host. Hence, callers of this method are responsible for issuing
        rescan operations to detect the new VMFS volume on other hosts.
        Alternatively, callers that want VirtualCenter to handle rescanning the
        necessary hosts should use the DatastoreSystem interface.When user wants
        to keep the original Vmfs Uuid and mount it on the host, set the
        'resolutionSpec.uuidResolution' to 'forceMounted' This is per-host
        operation. It will return an array of ResolutionResult describing success
        or failure associated with each specification.
        '''
        
        return self.delegate("ResolveMultipleUnresolvedVmfsVolumes")()
        

    def RetrieveDiskPartitionInfo(self):
        '''Gets the partition information for the disks named by the device names.
        '''
        
        return self.delegate("RetrieveDiskPartitionInfo")()
        

    def SetMultipathLunPolicy(self):
        '''Updates the path selection policy for a Logical Unit. Use the LUN uuid from
        HostMultipathInfoLogicalUnit.
        '''
        
        return self.delegate("SetMultipathLunPolicy")()
        

    def UnmountForceMountedVmfsVolume(self):
        '''Unmount the 'forceMounted' Vmfs volume. When a low level block copy is performed
        to copy or move the VMFS volume, the copied volume is unresolved. For the
        VMFS volume to be usable, a resolution operation is applied. As part of
        resolution operation, user may decide to keep the original VMFS Uuid. Once
        the resolution is applied, the VMFS volume is mounted on the host for its
        use. User can unmount the VMFS volume if it is not being used by any
        registered VMs.
        '''
        
        return self.delegate("UnmountForceMountedVmfsVolume")()
        

    def UpdateDiskPartitions(self):
        '''Changes the partitions on the disk by supplying a partition specification and the
        device name.
        '''
        
        return self.delegate("UpdateDiskPartitions")()
        

    def UpdateInternetScsiAdvancedOptions(self):
        '''Updates the advanced options the iSCSI host bus adapter or the discovery addresses
        and targets associated with it.
        '''
        
        return self.delegate("UpdateInternetScsiAdvancedOptions")()
        

    def UpdateInternetScsiAlias(self):
        '''Updates the alias of an iSCSI host bus adapter.
        '''
        
        return self.delegate("UpdateInternetScsiAlias")()
        

    def UpdateInternetScsiAuthenticationProperties(self):
        '''Updates the authentication properties for one or more targets or discovery
        addresses associated with an iSCSI host bus adapter.
        '''
        
        return self.delegate("UpdateInternetScsiAuthenticationProperties")()
        

    def UpdateInternetScsiDigestProperties(self):
        '''Updates the digest properties for the iSCSI host bus adapter or the discovery
        addresses and targets associated with it.
        '''
        
        return self.delegate("UpdateInternetScsiDigestProperties")()
        

    def UpdateInternetScsiDiscoveryProperties(self):
        '''Updates the Discovery properties for an iSCSI host bus adapter.
        '''
        
        return self.delegate("UpdateInternetScsiDiscoveryProperties")()
        

    def UpdateInternetScsiIPProperties(self):
        '''Updates the IP properties for an iSCSI host bus adapter.
        '''
        
        return self.delegate("UpdateInternetScsiIPProperties")()
        

    def UpdateInternetScsiName(self):
        '''Updates the name of an iSCSI host bus adapter.
        '''
        
        return self.delegate("UpdateInternetScsiName")()
        

    def UpdateScsiLunDisplayName(self):
        '''Update the mutable display name associated with a ScsiLun. The ScsiLun to be
        updated is identified using the specified uuid.
        '''
        
        return self.delegate("UpdateScsiLunDisplayName")()
        

    def UpdateSoftwareInternetScsiEnabled(self):
        '''Enables or disables Software iSCSI.
        '''
        
        return self.delegate("UpdateSoftwareInternetScsiEnabled")()
        

    def UpgradeVmfs(self):
        '''Upgrades the VMFS to the current VMFS version.
        '''
        
        return self.delegate("UpgradeVmfs")()
        

    def UpgradeVmLayout(self):
        '''Iterates over all registered virtual machines. For each VM which .vmx file is
        located on the service console and all disks are available on VMFS3 or
        NAS, it will relocate the disks into directories if stored in the ROOT,
        and relocate the VMX file into the directory too. Events are logged for
        each virtual machine that is relocated.
        '''
        
        return self.delegate("UpgradeVmLayout")()
        
