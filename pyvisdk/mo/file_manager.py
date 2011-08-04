
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class FileManager(BaseEntity):
    '''A URL has the form
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.FileManager):
        # MUST define these
        super(FileManager, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def ChangeOwner(self):
        '''Change the owner for a file.This method is currently not supported.
        '''
        
        return self.delegate("ChangeOwner")()
        

    def CopyDatastoreFile_Task(self, sourceName, sourceDatacenter, destinationName, destinationDatacenter, force):
        '''Copies the source file or folder to the destination.If the destination file does
        not exist, it is created. If the destination file exists, the force
        parameter determines whether to overwrite it with the source or not.
        Folders can be copied recursively. In this case, the destination, if it
        exists, must be a folder, else one will be created. Existing files on the
        destination that conflict with source files can be overwritten using the
        force parameter. Files and disks are always copied in binary format during
        recursive copy.If source (or destination) name is specified as a URL, then
        the corresponding datacenter parameter may be omitted.If any intermediate
        level folder specified by the source and destination does not exist, a
        FileNotFound fault is thrown.If a file of a virtual machine is overwritten
        on the destination datastore as a result of the force parameter, it may
        corrupt that virtual machine.If the source is an extent of a virtual disk,
        this operation treats the extent as a file.It is important to note that
        this operation will provide transactional guarantees only for a file. No
        guarantees are provided when copying a folder. If the intent is to clone a
        virtual machine registered in the inventory, with transactional
        guarantees, please refer to CloneVM_Task.Datastore.FileManagement
        privilege is required on both source and destination
        datastores.Experimental. Subject to change

        :param sourceName: The name of the source, either a URL or a datastore path referring to the file or
        folder to be copied.

        :param sourceDatacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when
        invoked directly on ESX. If not specified on a call to VirtualCenter,must
        be a URL.

        :param destinationName: The name of the destination, either a URL or a datastore path referring to the
        destination file or folder.

        :param destinationDatacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when
        invoked directly on ESX. If not specified on a call to VirtualCenter, it
        is assumed that the destination path belongs to the source datacenter.

        :param force: If true, overwrite any identically named file at the destination. If not
        specified, it is assumed to be false.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CopyDatastoreFile_Task")(sourceName,sourceDatacenter,destinationName,destinationDatacenter,force)
        

    def DeleteDatastoreFile_Task(self, name, datacenter):
        '''Deletes the specified file or folder from the datastore. If a file of a virtual
        machine is deleted, it may corrupt that virtual machine. Folder deletes
        are always recursive. The datacenter parameter may be omitted if a URL is
        used to name the file or folder.If the source is an extent of a virtual
        disk, this operation treats the extent as a file.It is important to note
        that this operation will provide transactional guarantees only for a file.
        No guarantees are provided when deleting folders. If the intent is to
        delete a virtual machine registered in the inventory, please refer to
        Destroy_Task.Requires Datastore.FileManagement privilege on the
        datastore.Experimental. Subject to change

        :param name: The name of the file or folder, either a URL or a datastore path referring to the
        file or folder to be deleted.

        :param datacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when
        invoked directly on ESX. If not specified on a call to VirtualCenter,must
        be a URL.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("DeleteDatastoreFile_Task")(name,datacenter)
        

    def MakeDirectory(self, name, datacenter, createParentDirectories):
        '''Create a folder using the specified name. If the parent or intermediate level
        folders do not exist, and the parameter createParentDirectories is false,
        a FileNotFound fault is thrown. If the intermediate level folders do not
        exist, and the parameter createParentDirectories is true, all the non-
        existent folders are created.Requires Datastore.FileManagement privilege
        on the datastore.Experimental. Subject to change

        :param name: The name of the folder, either a URL or a datastore path referring to the folder
        to be created.

        :param datacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when
        invoked directly on ESX. If not specified on a call to VirtualCenter,must
        be a URL.

        :param createParentDirectories: If true, any non-existent intermediate level folders will be created. If not
        specified, it is assumed to be false.

        '''
        
        return self.delegate("MakeDirectory")(name,datacenter,createParentDirectories)
        

    def MoveDatastoreFile_Task(self, sourceName, sourceDatacenter, destinationName, destinationDatacenter, force):
        '''Moves the source file or folder to the destination.If the destination file does
        not exist, it is created. If the destination file exists, the force
        parameter determines whether to overwrite it with the source or not. If
        the source path is a folder, then the destination path must not exist; the
        destination cannot be overwritten even with a force flag in that case.
        Folder moves are recursive, treating all files and disks to move as
        binary.If source (or destination) name is specified as a URL, then the
        corresponding datacenter parameter may be omitted.If any intermediate
        level folder specified by the source and destination does not exist, a
        FileNotFound fault is thrown.If a file of a virtual machine is moved, it
        may corrupt that virtual machine. If a file of a virtual machine is
        overwritten on the destination datastore as a result of the force
        parameter, it may corrupt that virtual machine.If the source is an extent
        of a virtual disk, this operation treats the extent as a file.It is
        important to note that this operation will provide transactional
        guarantees only for a file. No guarantees are provided for folder moves.
        If the intent is to move a virtual machine registered in the inventory,
        with transactional guarantees, please refer to RelocateVM_Task. If the
        intent is to rename a virtual machine registered in the inventory, please
        refer to Rename_Task.Datastore.FileManagement privilege is required on
        both source and destination datastores.Experimental. Subject to change

        :param sourceName: The name of the source, either a URL or a datastore path referring to the file or
        folder to be moved.

        :param sourceDatacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when
        invoked directly on ESX. If not specified on a call to VirtualCenter,must
        be a URL.

        :param destinationName: The name of the destination, either a URL or a datastore path referring to the
        destination file or folder.

        :param destinationDatacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when
        invoked directly on ESX. If not specified on a call to VirtualCenter, it
        is assumed that the destination path belongs to the source datacenter.

        :param force: If true, overwrite any identically named file at the destination. If not
        specified, it is assumed to be false.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("MoveDatastoreFile_Task")(sourceName,sourceDatacenter,destinationName,destinationDatacenter,force)
        
