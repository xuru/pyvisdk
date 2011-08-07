
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.managed_entity import ManagedEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class Folder(ManagedEntity):
    '''The Folder managed object is a container for storing and organizing inventory
        objects. Folders can contain folders and other objects. The childType
        property identifies a folder's type and determines the types of folders
        and objects the folder can contain.* A folder can contain a child folder
        of the same type as the parent folder. * All Datacenter objects contain
        dedicated folders for:See ServiceInstance for a representation of the
        organization of the inventory.The Folder managed object also acts as a
        factory object, meaning it creates new entities in a folder. The object
        provides methods to create child folders and objects, methods to add
        existing objects to folders, and methods to remove objects from folders
        and to delete folders.Folder inherits the Destroy_Task method.
        Destroy_Task is a recursive operation that removes all child objects and
        folders. When you call Destroy_Task to destroy a folder, the system uses
        the specified folder as a root and traverses its descendant hierarchy,
        calling Destroy_Task on each object. Destroy_Task is a single operation
        that treats each recursive call as a single transaction, committing each
        call to remove an object individually. If Destroy_Task fails on an object,
        the method terminates at that point with an exception, leaving some or all
        of the objects still in the inventory.Notes on the folder destroy method:
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.Folder):
        # MUST define these
        super(Folder, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def AddStandaloneHost_Task(self):
        '''Creates a new single-host compute resource. The name provided can be an IP
        address, such as 192.168.0.120, or a string, such as esx120. If a name is
        specified, a DNS lookup is used to resolve it to a fully-qualified name,
        such as esx120.vmware.com. If the DNS lookup fails, the string is stored
        as specified.Licenses for the host are allocated when making the first
        connection to the host. This is because the license needed typically
        depends on the type of host and the number of CPUs.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("AddStandaloneHost_Task")()
        

    def CreateCluster(self):
        '''Deprecated. As of VI API 2.5, use CreateClusterEx. Creates a new cluster compute
        resource in this folder.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CreateCluster")()
        

    def CreateClusterEx(self):
        '''Creates a new cluster compute resource in this folder.Any % (percent) character
        used in this name parameter must be escaped, unless it is used to start an
        escape sequence. Clients may also escape any other characters in this name
        parameter.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CreateClusterEx")()
        

    def CreateDatacenter(self):
        '''Creates a new datacenter with the given name.Any % (percent) character used in
        this name parameter must be escaped, unless it is used to start an escape
        sequence. Clients may also escape any other characters in this name
        parameter.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CreateDatacenter")()
        

    def CreateDVS_Task(self):
        '''Create a Distributed Virtual Switch in the folder according to the specified
        (@link vim.DistributedVirtualSwitch.CreateSpec).

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CreateDVS_Task")()
        

    def CreateFolder(self):
        '''Creates a new sub-folder with the specified name. The childType property of the
        new folder is the same as the childType property of the current folder.Any
        % (percent) character used in this name parameter must be escaped, unless
        it is used to start an escape sequence. Clients may also escape any other
        characters in this name parameter.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CreateFolder")()
        

    def CreateVM_Task(self):
        '''Creates a new virtual machine in the current folder and attaches it to the
        specified resource pool. This operation creates a virtual machine, instead
        of cloning a virtual machine from an existing one.The server does not
        support creating templates using this method. Instead, you should create
        templates by marking existing virtual machines as templates, or by cloning
        an existing virtual machine or template.This operation only works if the
        folder's childType includes VirtualMachine. In addition to the
        VirtualMachine.Inventory.Create privilege, may also require any of the
        following privileges depending on the properties of the virtual machine
        bring created:

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CreateVM_Task")()
        

    def MoveIntoFolder_Task(self):
        '''Moves a set of managed entities into this folder.This operation is typically used
        by clients when they implement a drag-and-drop interface to move a set of
        objects into a folder.This operation is transactional only with respect to
        each individual entity. The set of entities is moved sequentially as
        specified in the list, and committed one at a time. If the
        MoveIntoFolder_Task method fails on an object, the method terminates at
        that point with an exception, leaving the rest of the managed entities in
        their original location.The objects that can be moved into a folder
        depends on the folder's type (as defined by the folder's childType
        property). For a datacenter folder, only datacenters and datacenter
        folders can be moved into the folder. For a virtual machine folder, only
        virtual machines and virtual machine folders can be moved into the folder.
        For a host folder, ComputeResource objects, host folder objects, and
        HostSystem objects can be moved into the folder.Moving a HostSystem into a
        host folder creates a stand-alone host from a host that is currently part
        of a ClusterComputeResource. The host must be part of a
        ClusterComputeResource in the same datacenter and the host must be in
        maintenance mode. Otherwise, the operation fails.A ComputeResource with a
        single root resource pool is created for each HostSystem. The name of the
        ComputeResource is the DNS or IP address of the host. This operation moves
        the (physical) host resources out of a cluster. It does not move or change
        the ResourcePool configuration that is part of the ClusterComputeResource
        with which the host was associated.Note that all virtual machines
        associated with a host are moved with the host into the folder. If there
        are virtual machines that should not be moved with the host, then migrate
        them from the host before initiating this operation.For a HostSystem move,
        the privileges required are Host.Inventory.EditCluster on the source
        ClusterComputeResource, Host.Inventory.MoveHost on the HostSystem, and
        Host.Inventory.AddStandaloneHost on the target Folder.Otherwise, the
        privilege required for this operation varies depending on this folder's
        type and is checked against the source container, destination container,
        and the object:If the object is a HostSystem, the privileges required are
        Host.Inventory.AddStandaloneHost on the folder, Host.Inventory.MoveHost on
        the HostSystem, and Host.Inventory.EditCluster on the host's original
        ComputeResource.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("MoveIntoFolder_Task")()
        

    def RegisterVM_Task(self):
        '''Adds an existing virtual machine to the folder.Any % (percent) character used in
        this name parameter must be escaped, unless it is used to start an escape
        sequence. Clients may also escape any other characters in this name
        parameter.This operation only works if the folder's type is
        VirtualMachine.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("RegisterVM_Task")()
        

    def UnregisterAndDestroy_Task(self):
        '''Recursively unregisters all virtual machines and vApps, and destroys all child
        virtual machine folders. This is similar to the Destroy_Task method, but
        this method calls UnregisterAndDestroy_Task on each virtual machine object
        instead of calling Destroy_Task. This operation applies only to
        VirtualMachine folders.UnregisterAndDestroy_Task is a recursive operation
        that destroys the specified virtual machine folder, unregisters all child
        virtual machine objects, and destroys all child virtual machine folders.
        When you call UnregisterAndDestroy_Task to destroy a virtual machine
        folder, the system uses the specified folder as a root and traverses its
        descendant hierarchy, calling UnregisterAndDestroy_Task on each virtual
        machine object and Destroy_Task on each virtual machine folder.
        UnregisterAndDestroy_Task is a single operation that treats each recursive
        call as a single transaction, committing each call to remove an object
        individually. If a failure occurs, the method terminates at that point
        with an exception, leaving some or all objects unaffected.If you are
        removing virtual machines, you must hold the VirtualMachine.Delete
        privilege on all of the virtual machines to be unregistered, and on their
        parent folders. If you are removing virtual applications, you must hold
        the VApp.Delete privilege on all of the virtual applications to be
        unregistered, and on their parent folders.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("UnregisterAndDestroy_Task")()
        
