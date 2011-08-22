
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.base_entity import BaseEntity
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
    interface. See Datastore'''
    
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
    
    
    
    def ConfigureDatastorePrincipal(self):
        '''Configures datastore principal user for the host.All virtual machine-related
        file I/O is performed under this user. Configuring datastore principal user
        will result in all virtual machine files (configuration, disk, and so on) being
        checked for proper access. If necessary, ownership and permissions are
        modified. Note that in some environments, file ownership and permissions
        modification may not be possible. For example, virtual machine files stored on
        NFS cannot be modified for ownership and permissions if root squashing is
        enabled. Ownership and permissions for these files must be manually changed by
        a system administrator. In general, if server process does not have rights to
        change ownership and file permissions of virtual machine files, they must be
        modified manually. If a virtual machine files are not read/writeable by this
        user, virtual machine related operations such as power on/off, configuration,
        and so on will fail. This operation must be performed while in maintenance mode
        and requires host reboot.
        :rtype: None
        :returns: 
        '''
        return self.delegate("ConfigureDatastorePrincipal")()
    
    def CreateLocalDatastore(self):
        '''Creates a new local datastore.
        :rtype: ManagedObjectReference to a Datastore
        :returns: 
        '''
        return self.delegate("CreateLocalDatastore")()
    
    def CreateNasDatastore(self):
        '''Creates a new network-attached storage datastore.
        :rtype: ManagedObjectReference to a Datastore
        :returns: 
        '''
        return self.delegate("CreateNasDatastore")()
    
    def CreateVmfsDatastore(self):
        '''Creates a new VMFS datastore.
        :rtype: ManagedObjectReference to a Datastore
        :returns: 
        '''
        return self.delegate("CreateVmfsDatastore")()
    
    def ExpandVmfsDatastore(self):
        '''Increases the capacity of an existing VMFS datastore by expanding (increasing
        the size of) an existing extent of the datastore.
        :rtype: ManagedObjectReference to a Datastore
        :returns: 
        '''
        return self.delegate("ExpandVmfsDatastore")()
    
    def ExtendVmfsDatastore(self):
        '''Increases the capacity of an existing VMFS datastore by adding new extents to
        the datastore.
        :rtype: ManagedObjectReference to a Datastore
        :returns: 
        '''
        return self.delegate("ExtendVmfsDatastore")()
    
    def QueryAvailableDisksForVmfs(self):
        '''Query to list disks that can be used to contain VMFS datastore extents. If the
        optional parameter name is supplied, queries for disks that can be used to
        contain extents for a VMFS datastore identified by the supplied name.
        Otherwise, the method retrieves disks that can be used to contain new VMFS
        datastores.This operation will filter out disks that are currently in use by an
        existing VMFS unless the VMFS using the disk is one being extended. It will
        also filter out management LUNs and disks that are referenced by RDMs. These
        disk LUNs are also unsuited for use by a VMFS.Disk LUNs referenced by RDMs are
        found by examining all virtual machines known to the system and visiting their
        virtual disk backends. If a virtual disk backend uses an RDM that is
        referencing a disk LUN, the disk LUN becomes ineligible for use by a VMFS
        datastore.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryAvailableDisksForVmfs")()
    
    def QueryUnresolvedVmfsVolumes(self):
        '''Get the list of unbound VMFS volumes. For sharing a volume across hosts, a VMFS
        volume is bound to its underlying block device storage. When a low level block
        copy is performed to copy or move the VMFS volume, the copied volume will be
        unbound.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryUnresolvedVmfsVolumes")()
    
    def QueryVmfsDatastoreCreateOptions(self):
        '''Queries options for creating a new VMFS datastore for a disk. See devicePath
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryVmfsDatastoreCreateOptions")()
    
    def QueryVmfsDatastoreExpandOptions(self):
        '''Queries for options for increasing the capacity of an existing VMFS datastore
        by expanding (increasing the size of) an existing extent of the datastore.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryVmfsDatastoreExpandOptions")()
    
    def QueryVmfsDatastoreExtendOptions(self):
        '''Queries for options for increasing the capacity of an existing VMFS datastore
        by adding new extents using space from the specified disk. See devicePath
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryVmfsDatastoreExtendOptions")()
    
    def RemoveDatastore(self):
        '''Removes a datastore from a host.
        :rtype: None
        :returns: 
        '''
        return self.delegate("RemoveDatastore")()
    
    def ResignatureUnresolvedVmfsVolume_Task(self):
        '''Resignature an unbound VMFS volume. To safely enable sharing of the volume
        across hosts, a VMFS volume is bound to its underlying block device storage.
        When a low level block copy is performed to copy or move the VMFS volume, the
        copied volume will be unbound. In order for the VMFS volume to be usable, a
        resolution operation is needed to determine whether the VMFS volume should be
        treated as a new volume or not and what extents compose that volume in the
        event there is more than one unbound volume.With 'Resignature' operation, a new
        Vmfs Uuid is assigned to the volume but its contents are kept intact.
        Resignature results in a new Vmfs volume on the host. Users can specify a list
        of hosts on which the volume will be auto-mounted.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("ResignatureUnresolvedVmfsVolume_Task")()
    
    def UpdateLocalSwapDatastore(self):
        '''Choose the localSwapDatastore for this host. Any change to this setting will
        affect virtual machines that subsequently power on or resume from a suspended
        state at this host, or that migrate to this host while powered on; virtual
        machines that are currently powered on at this host will not yet be affected.
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdateLocalSwapDatastore")()