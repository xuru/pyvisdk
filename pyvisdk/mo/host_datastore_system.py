
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDatastoreSystem(BaseEntity):
    '''This managed object creates and removes datastores from the host.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostDatastoreSystem):
        # MUST define these
        super(HostDatastoreSystem, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def ConfigureDatastorePrincipal(self, userName):
        '''Configures datastore principal user for the host.All virtual machine-related file
        I/O is performed under this user. Configuring datastore principal user
        will result in all virtual machine files (configuration, disk, and so on)
        being checked for proper access. If necessary, ownership and permissions
        are modified. Note that in some environments, file ownership and
        permissions modification may not be possible. For example, virtual machine
        files stored on NFS cannot be modified for ownership and permissions if
        root squashing is enabled. Ownership and permissions for these files must
        be manually changed by a system administrator. In general, if server
        process does not have rights to change ownership and file permissions of
        virtual machine files, they must be modified manually. If a virtual
        machine files are not read/writeable by this user, virtual machine related
        operations such as power on/off, configuration, and so on will fail. This
        operation must be performed while in maintenance mode and requires host
        reboot.

        :param userName: Datastore principal user name.

        '''
        
        return self.delegate("ConfigureDatastorePrincipal")(userName)
        

    def QueryVmfsDatastoreCreateOptions(self):
        '''Queries options for creating a new VMFS datastore for a disk. See devicePath

        :rtype: VmfsDatastoreOption[] 

        '''
        
        return self.delegate("QueryVmfsDatastoreCreateOptions")()
        

    def UpdateLocalSwapDatastore(self):
        '''Choose the localSwapDatastore for this host. Any change to this setting will
        affect virtual machines that subsequently power on or resume from a
        suspended state at this host, or that migrate to this host while powered
        on; virtual machines that are currently powered on at this host will not
        yet be affected.
        '''
        
        return self.delegate("UpdateLocalSwapDatastore")()
        

    def QueryVmfsDatastoreExtendOptions(self):
        '''Queries for options for increasing the capacity of an existing VMFS datastore by
        adding new extents using space from the specified disk. See devicePath

        :rtype: VmfsDatastoreOption[] 

        '''
        
        return self.delegate("QueryVmfsDatastoreExtendOptions")()
        

    def CreateNasDatastore(self, spec):
        '''Creates a new network-attached storage datastore.

        :param spec: The specification for creating a network-attached storage volume.


        :rtype: ManagedObjectReference to a Datastore 

        '''
        
        return self.delegate("CreateNasDatastore")(spec)
        

    def ExtendVmfsDatastore(self, spec):
        '''Increases the capacity of an existing VMFS datastore by adding new extents to the
        datastore.

        :param spec: The specification describing what extents to add to a VMFS datastore.


        :rtype: ManagedObjectReference to a Datastore 

        '''
        
        return self.delegate("ExtendVmfsDatastore")(spec)
        

    def CreateVmfsDatastore(self, spec):
        '''Creates a new VMFS datastore.

        :param spec: The specification for creating a datastore backed by a VMFS.


        :rtype: ManagedObjectReference to a Datastore 

        '''
        
        return self.delegate("CreateVmfsDatastore")(spec)
        

    def CreateLocalDatastore(self, path, name):
        '''Creates a new local datastore.

        :param path: The file path for a directory in which the virtual machine data will be stored.

        :param name: The name of a datastore to create on the local host.


        :rtype: ManagedObjectReference to a Datastore 

        '''
        
        return self.delegate("CreateLocalDatastore")(path,name)
        

    def QueryAvailableDisksForVmfs(self):
        '''Query to list disks that can be used to contain VMFS datastore extents. If the
        optional parameter name is supplied, queries for disks that can be used to
        contain extents for a VMFS datastore identified by the supplied name.
        Otherwise, the method retrieves disks that can be used to contain new VMFS
        datastores.This operation will filter out disks that are currently in use
        by an existing VMFS unless the VMFS using the disk is one being extended.
        It will also filter out management LUNs and disks that are referenced by
        RDMs. These disk LUNs are also unsuited for use by a VMFS.Disk LUNs
        referenced by RDMs are found by examining all virtual machines known to
        the system and visiting their virtual disk backends. If a virtual disk
        backend uses an RDM that is referencing a disk LUN, the disk LUN becomes
        ineligible for use by a VMFS datastore.

        :rtype: HostScsiDisk[] 

        '''
        
        return self.delegate("QueryAvailableDisksForVmfs")()
        

    def ExpandVmfsDatastore(self, spec):
        '''Increases the capacity of an existing VMFS datastore by expanding (increasing the
        size of) an existing extent of the datastore.

        :param spec: The specification describing which extent of the VMFS datastore to expand.


        :rtype: ManagedObjectReference to a Datastore 

        '''
        
        return self.delegate("ExpandVmfsDatastore")(spec)
        

    def RemoveDatastore(self):
        '''Removes a datastore from a host.
        '''
        
        return self.delegate("RemoveDatastore")()
        

    def QueryVmfsDatastoreExpandOptions(self):
        '''Queries for options for increasing the capacity of an existing VMFS datastore by
        expanding (increasing the size of) an existing extent of the datastore.

        :rtype: VmfsDatastoreOption[] 

        '''
        
        return self.delegate("QueryVmfsDatastoreExpandOptions")()
        

    def ResignatureUnresolvedVmfsVolume_Task(self, resolutionSpec):
        '''Resignature an unbound VMFS volume. To safely enable sharing of the volume across
        hosts, a VMFS volume is bound to its underlying block device storage. When
        a low level block copy is performed to copy or move the VMFS volume, the
        copied volume will be unbound. In order for the VMFS volume to be usable,
        a resolution operation is needed to determine whether the VMFS volume
        should be treated as a new volume or not and what extents compose that
        volume in the event there is more than one unbound volume.With
        'Resignature' operation, a new Vmfs Uuid is assigned to the volume but its
        contents are kept intact. Resignature results in a new Vmfs volume on the
        host. Users can specify a list of hosts on which the volume will be auto-
        mounted.

        :param resolutionSpec: A data object that describes what the disk extents to be used for creating the new VMFS volume.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("ResignatureUnresolvedVmfsVolume_Task")(resolutionSpec)
        

    def QueryUnresolvedVmfsVolumes(self):
        '''Get the list of unbound VMFS volumes. For sharing a volume across hosts, a VMFS
        volume is bound to its underlying block device storage. When a low level
        block copy is performed to copy or move the VMFS volume, the copied volume
        will be unbound.

        :rtype: HostUnresolvedVmfsVolume[] 

        '''
        
        return self.delegate("QueryUnresolvedVmfsVolumes")()
        
