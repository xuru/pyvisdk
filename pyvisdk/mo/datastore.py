
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.managed_entity import ManagedEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class Datastore(ManagedEntity):
    '''Any reference to a virtual machine or file accessed by any host within the
        datacenter must use a datastore path. A datastore path has the form
        "[<datastore>] <path>", where <datastore> is the datastore name, and
        <path> is a slash-delimited path from the root of the datastore. An
        example datastore path is "[storage] path/to/config.vmx".
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.Datastore):
        # MUST define these
        super(Datastore, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def browser(self):
        '''DatastoreBrowser used to browse this datastore.
        '''
        return self.update('browser')

    @property
    def capability(self):
        '''Capabilities of this datastore.
        '''
        return self.update('capability')

    @property
    def host(self):
        '''Hosts attached to this datastore.
        '''
        return self.update('host')

    @property
    def info(self):
        '''Specific information about the datastore.
        '''
        return self.update('info')

    @property
    def iormConfiguration(self):
        '''Configuration of storage I/O resource management for the datastore. Currently we
        only support storage I/O resource management on VMFS volumes of a
        datastore.
        '''
        return self.update('iormConfiguration')

    @property
    def summary(self):
        '''Global properties of the datastore.
        '''
        return self.update('summary')

    @property
    def vm(self):
        '''Virtual machines stored on this datastore.
        '''
        return self.update('vm')


    def DestroyDatastore(self):
        '''Deprecated. As of VI API 2.5 do not use this method. This method throws
        ResourceInUse. Datastores are automatically removed when no longer in use,
        so this method is unnecessary. Removes a datastore. A datastore can be
        removed only if it is not currently used by any host or virtual machine.
        '''
        
        return self.delegate("DestroyDatastore")()
        

    def RefreshDatastore(self):
        '''Explicitly refreshes free-space and capacity values in summary and info.
        '''
        
        return self.delegate("RefreshDatastore")()
        

    def RefreshDatastoreStorageInfo(self):
        '''Refreshes all storage related information including free-space, capacity, and
        detailed usage of virtual machines. Updated values are available in
        summary and info.
        '''
        
        return self.delegate("RefreshDatastoreStorageInfo")()
        

    def RenameDatastore(self, newName):
        '''Deprecated. As of vSphere API 4.0, use Rename_Task. Renames a datastore.

        :param newName: The new name to assign to the datastore.

        '''
        
        return self.delegate("RenameDatastore")(newName)
        

    def UpdateVirtualMachineFiles_Task(self, mountPathDatastoreMapping):
        '''Update file paths embedded in virtual machine files on the datastore. This can be
        called after the file system corresponding to the datastore has been
        resignatured or remounted.This method is only supported by vCenter
        server.While this operation is in progress, it is important that users do
        not initiate any operations that might read or write to any files on the
        datastore, such as registering a virtual machine with files residing on
        the datastore, or performing any virtual disk operations on any files in
        the datastore. These operations can potentially cause spurious file update
        failures, while at the same time they can prevent virtual machine files
        from being updated correctly.If users intend to update multiple datastores
        using this method, it is strongly advised that the users do not initiate
        any operations that might read or write to files on any of the datastores,
        until all of them have been updated. The files of a single virtual machine
        can reside on multiple datastores, and thus all the involved datastores
        should be updated, before the virtual machine is considered updated
        completely.

        :param mountPathDatastoreMapping: Old mount path to datastore mapping.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("UpdateVirtualMachineFiles_Task")(mountPathDatastoreMapping)
        
