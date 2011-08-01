
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
        and objects the folder can contain.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.Folder):
        # MUST define these
        super(Folder, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def childType(self):
        '''
        Specifies the object types a folder may contain. When you create a folder, it
        inherits its childType from the parent folder in which it is created.
        childType is an array of strings. Each array entry identifies a set of
        object types - Folder and one or more managed object types. The following
        list shows childType values for the different folders:
        '''
        return self.update('childType')


    def CreateVM_Task(self, config):
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

        :param config: The configuration of the virtual machine hardware.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CreateVM_Task")(config)
        

    def RegisterVM_Task(self, path, asTemplate):
        '''Adds an existing virtual machine to the folder.Any % (percent) character used in
        this name parameter must be escaped, unless it is used to start an escape
        sequence. Clients may also escape any other characters in this name
        parameter.This operation only works if the folder's type is
        VirtualMachine.

        :param path: A datastore path to the virtual machine.

        :param asTemplate: Flag to specify whether or not the virtual machine should be marked as a template.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("RegisterVM_Task")(path,asTemplate)
        

    def CreateDVS_Task(self, spec):
        '''Create a Distributed Virtual Switch in the folder according to the specified
        (@link vim.DistributedVirtualSwitch.CreateSpec).

        :param spec: The (@link vim.DistributedVirtualSwitch.CreateSpec) to create the Distributed Virtual Switch.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CreateDVS_Task")(spec)
        

    def CreateClusterEx(self, name, spec):
        '''Creates a new cluster compute resource in this folder.Any % (percent) character
        used in this name parameter must be escaped, unless it is used to start an
        escape sequence. Clients may also escape any other characters in this name
        parameter.

        :param name: Name for the new cluster.

        :param spec: Specification for the cluster.


        :rtype: ManagedObjectReference to a ClusterComputeResource 

        '''
        
        return self.delegate("CreateClusterEx")(name,spec)
        

    def CreateCluster(self, name, spec):
        '''Deprecated. As of VI API 2.5, use CreateClusterEx. Creates a new cluster compute
        resource in this folder.

        :param name: Name for the new cluster.

        :param spec: Specification for the cluster.


        :rtype: ManagedObjectReference to a ClusterComputeResource 

        '''
        
        return self.delegate("CreateCluster")(name,spec)
        

    def CreateFolder(self, name):
        '''Creates a new sub-folder with the specified name. The childType property of the
        new folder is the same as the childType property of the current folder.Any
        % (percent) character used in this name parameter must be escaped, unless
        it is used to start an escape sequence. Clients may also escape any other
        characters in this name parameter.

        :param name: The name to be given the new folder. An entity name must be a non-empty string of less than 80 characters. The slash (/), backslash (\) and percent (%) will be escaped using the URL syntax. For example, %2F.


        :rtype: ManagedObjectReference to a Folder 

        '''
        
        return self.delegate("CreateFolder")(name)
        

    def AddStandaloneHost_Task(self, spec, addConnected):
        '''Creates a new single-host compute resource. The name provided can be an IP
        address, such as 192.168.0.120, or a string, such as esx120. If a name is
        specified, a DNS lookup is used to resolve it to a fully-qualified name,
        such as esx120.vmware.com. If the DNS lookup fails, the string is stored
        as specified.Licenses for the host are allocated when making the first
        connection to the host. This is because the license needed typically
        depends on the type of host and the number of CPUs.

        :param spec: The host name, port, and passwords for the host to be added.

        :param addConnected: Flag to specify whether or not the host should be connected as soon as it is added. The creation operation fails if a connection attempt is made and fails.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("AddStandaloneHost_Task")(spec,addConnected)
        

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
        and the object:

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("MoveIntoFolder_Task")()
        

    def CreateDatacenter(self, name):
        '''Creates a new datacenter with the given name.Any % (percent) character used in
        this name parameter must be escaped, unless it is used to start an escape
        sequence. Clients may also escape any other characters in this name
        parameter.

        :param name: Name for the new datacenter. An entity name must be a non-empty string of less than 80 characters. The slash (/), backslash (\) and percent (%) will be escaped using the URL syntax. For example, %2F.


        :rtype: ManagedObjectReference to a Datacenter 

        '''
        
        return self.delegate("CreateDatacenter")(name)
        

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
        
