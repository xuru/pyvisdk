
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDatastoreSystem(BaseEntity):
    '''This managed object creates and removes datastores from the host.To a host, a
    datastore is a storage abstraction that is backed by one of several types of
    storage volumes:An ESX Server system automatically discovers the VMFS volume on
    attached Logical Unit Numbers (LUNs) on startup and after re-scanning the host
    bus adapter. Datastores are automatically created. The datastore label is based
    on the VMFS volume label. If there is a conflict with an existing datastore, it
    is made unique by appending a suffix. The VMFS volume label will be
    unchanged.Destroying the datastore removes the partitions that compose the VMFS
    volume.Datastores are never automatically removed because transient storage
    connection outages may occur. They must be removed from the host using this
    interface.See Datastore'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostDatastoreSystem):
        super(HostDatastoreSystem, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def capabilities(self):
        '''Capability vector indicating the available product features.'''
        return self.update('capabilities')
    @property
    def datastore(self):
        '''List of datastores on this host.'''
        return self.update('datastore')

    
    
    def ConfigureDatastorePrincipal(self, userName, password=None):
        '''Configures datastore principal user for the host.Configures datastore principal
        user for the host.
        
        :param userName: Datastore principal user name.
        
        :param password: Optional password for systems that require password for user impersonation.
        
        '''
        return self.delegate("ConfigureDatastorePrincipal")(userName, password)
    
    def CreateLocalDatastore(self, name, path):
        '''Creates a new local datastore.
        
        :param name: The name of a datastore to create on the local host.
        
        :param path: The file path for a directory in which the virtual machine data will be stored.
        
        '''
        return self.delegate("CreateLocalDatastore")(name, path)
    
    def CreateNasDatastore(self, spec):
        '''Creates a new network-attached storage datastore.
        
        :param spec: The specification for creating a network-attached storage volume.
        
        '''
        return self.delegate("CreateNasDatastore")(spec)
    
    def CreateVmfsDatastore(self, spec):
        '''Creates a new VMFS datastore.
        
        :param spec: The specification for creating a datastore backed by a VMFS.
        
        '''
        return self.delegate("CreateVmfsDatastore")(spec)
    
    def ExpandVmfsDatastore(self, datastore, spec):
        '''Increases the capacity of an existing VMFS datastore by expanding (increasing
        the size of) an existing extent of the datastore.
        
        :param datastore: The datastore whose capacity should be increased.
        
        :param spec: The specification describing which extent of the VMFS datastore to expand.
        
        '''
        return self.delegate("ExpandVmfsDatastore")(datastore, spec)
    
    def ExtendVmfsDatastore(self, datastore, spec):
        '''Increases the capacity of an existing VMFS datastore by adding new extents to
        the datastore.
        
        :param datastore: The datastore whose capacity should be increased.
        
        :param spec: The specification describing what extents to add to a VMFS datastore.
        
        '''
        return self.delegate("ExtendVmfsDatastore")(datastore, spec)
    
    def QueryAvailableDisksForVmfs(self, datastore=None):
        '''Query to list disks that can be used to contain VMFS datastore extents. If the
        optional parameter name is supplied, queries for disks that can be used to
        contain extents for a VMFS datastore identified by the supplied name.
        Otherwise, the method retrieves disks that can be used to contain new VMFS
        datastores.Query to list disks that can be used to contain VMFS datastore
        extents. If the optional parameter name is supplied, queries for disks that can
        be used to contain extents for a VMFS datastore identified by the supplied
        name. Otherwise, the method retrieves disks that can be used to contain new
        VMFS datastores.Query to list disks that can be used to contain VMFS datastore
        extents. If the optional parameter name is supplied, queries for disks that can
        be used to contain extents for a VMFS datastore identified by the supplied
        name. Otherwise, the method retrieves disks that can be used to contain new
        VMFS datastores.
        
        :param datastore: The managed object reference of the VMFS datastore you want extents for.
        
        '''
        return self.delegate("QueryAvailableDisksForVmfs")(datastore)
    
    def QueryUnresolvedVmfsVolumes(self):
        '''Get the list of unbound VMFS volumes. For sharing a volume across hosts, a VMFS
        volume is bound to its underlying block device storage. When a low level block
        copy is performed to copy or move the VMFS volume, the copied volume will be
        unbound.
        
        '''
        return self.delegate("QueryUnresolvedVmfsVolumes")()
    
    def QueryVmfsDatastoreCreateOptions(self, devicePath, vmfsMajorVersion=None):
        '''Queries options for creating a new VMFS datastore for a disk.See devicePath
        
        :param devicePath: The devicePath of the disk on which datastore creation options are generated.See devicePath
        
        :param vmfsMajorVersion: major version of VMFS to be used for formatting the datastore. If this parameter is not specified, then the default VMFS version for the host is used.See devicePathvSphere API 5.0
        
        '''
        return self.delegate("QueryVmfsDatastoreCreateOptions")(devicePath, vmfsMajorVersion)
    
    def QueryVmfsDatastoreExpandOptions(self, datastore):
        '''Queries for options for increasing the capacity of an existing VMFS datastore
        by expanding (increasing the size of) an existing extent of the datastore.
        
        :param datastore: The datastore to be expanded.
        
        '''
        return self.delegate("QueryVmfsDatastoreExpandOptions")(datastore)
    
    def QueryVmfsDatastoreExtendOptions(self, datastore, devicePath, suppressExpandCandidates=None):
        '''Queries for options for increasing the capacity of an existing VMFS datastore
        by adding new extents using space from the specified disk.See devicePath
        
        :param datastore: The datastore to be extended.See devicePath
        
        :param devicePath: The devicePath of the disk on which datastore extension options are generated.See devicePath
        
        :param suppressExpandCandidates: Indicates whether to exclude options that can be used for extent expansion also. Free space can be used for adding an extent or expanding an existing extent. If this parameter is set to true, the list of options returned will not include free space that can be used for expansion.See devicePathvSphere API 4.0
        
        '''
        return self.delegate("QueryVmfsDatastoreExtendOptions")(datastore, devicePath, suppressExpandCandidates)
    
    def RemoveDatastore(self, datastore):
        '''Removes a datastore from a host.
        
        :param datastore: The datastore to be removed.
        
        '''
        return self.delegate("RemoveDatastore")(datastore)
    
    def ResignatureUnresolvedVmfsVolume_Task(self, resolutionSpec):
        '''Resignature an unbound VMFS volume. To safely enable sharing of the volume
        across hosts, a VMFS volume is bound to its underlying block device storage.
        When a low level block copy is performed to copy or move the VMFS volume, the
        copied volume will be unbound. In order for the VMFS volume to be usable, a
        resolution operation is needed to determine whether the VMFS volume should be
        treated as a new volume or not and what extents compose that volume in the
        event there is more than one unbound volume.Resignature an unbound VMFS volume.
        To safely enable sharing of the volume across hosts, a VMFS volume is bound to
        its underlying block device storage. When a low level block copy is performed
        to copy or move the VMFS volume, the copied volume will be unbound. In order
        for the VMFS volume to be usable, a resolution operation is needed to determine
        whether the VMFS volume should be treated as a new volume or not and what
        extents compose that volume in the event there is more than one unbound volume.
        
        :param resolutionSpec: A data object that describes what the disk extents to be used for creating the new VMFS volume.
        
        '''
        return self.delegate("ResignatureUnresolvedVmfsVolume_Task")(resolutionSpec)
    
    def UpdateLocalSwapDatastore(self, datastore=None):
        '''Choose the localSwapDatastore for this host. Any change to this setting will
        affect virtual machines that subsequently power on or resume from a suspended
        state at this host, or that migrate to this host while powered on; virtual
        machines that are currently powered on at this host will not yet be affected.
        
        :param datastore: The selected datastore. If this argument is unset, then the localSwapDatastore property becomes unset. Otherwise, the host must have read/write access to the indicated datastore.
        
        '''
        return self.delegate("UpdateLocalSwapDatastore")(datastore)