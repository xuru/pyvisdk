
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class FileManager(BaseEntity):
    '''This managed object type provides a way to manage and manipulate files and
    folders on datastores. The source and the destination names are in the form of
    a URL or a datastore path.A URL has the formwhere* is or . * specifies the
    hostname or IP address of the VirtualCenter or ESX server and optionally the
    port. * is the inventory path to the Datacenter containing the Datastore. * is
    the name of the Datastore. * is a slash-delimited path from the root of the
    datastore.A datastore path has the formwhere* is the datastore name. * is a
    slash-delimited path from the root of the datastore.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.FileManager):
        super(FileManager, self).__init__(core, name=name, ref=ref, type=type)

    

    
    
    def ChangeOwner(self, name, owner, datacenter=None):
        '''Change the owner for a file.Change the owner for a file.
        
        :param name: 
        
        :param datacenter: 
        
        :param owner: 
        
        '''
        return self.delegate("ChangeOwner")(name, datacenter, owner)
    
    def CopyDatastoreFile_Task(self, sourceName, destinationName, sourceDatacenter=None, destinationDatacenter=None, force=None):
        '''Copies the source file or folder to the destination.Copies the source file or
        folder to the destination.Copies the source file or folder to the
        destination.Copies the source file or folder to the destination.Copies the
        source file or folder to the destination.Copies the source file or folder to
        the destination.Copies the source file or folder to the destination.Copies the
        source file or folder to the destination.Copies the source file or folder to
        the destination.
        
        :param sourceName: The name of the source, either a URL or a datastore path referring to the file or folder to be copied.
        
        :param sourceDatacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,must be a URL.
        
        :param destinationName: The name of the destination, either a URL or a datastore path referring to the destination file or folder.
        
        :param destinationDatacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter, it is assumed that the destination path belongs to the source datacenter.
        
        :param force: If true, overwrite any identically named file at the destination. If not specified, it is assumed to be false.
        
        '''
        return self.delegate("CopyDatastoreFile_Task")(sourceName, sourceDatacenter, destinationName, destinationDatacenter, force)
    
    def DeleteDatastoreFile_Task(self, name, datacenter=None):
        '''Deletes the specified file or folder from the datastore. If a file of a virtual
        machine is deleted, it may corrupt that virtual machine. Folder deletes are
        always recursive. The datacenter parameter may be omitted if a URL is used to
        name the file or folder.Deletes the specified file or folder from the
        datastore. If a file of a virtual machine is deleted, it may corrupt that
        virtual machine. Folder deletes are always recursive. The datacenter parameter
        may be omitted if a URL is used to name the file or folder.Deletes the
        specified file or folder from the datastore. If a file of a virtual machine is
        deleted, it may corrupt that virtual machine. Folder deletes are always
        recursive. The datacenter parameter may be omitted if a URL is used to name the
        file or folder.Deletes the specified file or folder from the datastore. If a
        file of a virtual machine is deleted, it may corrupt that virtual machine.
        Folder deletes are always recursive. The datacenter parameter may be omitted if
        a URL is used to name the file or folder.
        
        :param name: The name of the file or folder, either a URL or a datastore path referring to the file or folder to be deleted.
        
        :param datacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,must be a URL.
        
        '''
        return self.delegate("DeleteDatastoreFile_Task")(name, datacenter)
    
    def MakeDirectory(self, name, datacenter=None, createParentDirectories=None):
        '''Create a folder using the specified name. If the parent or intermediate level
        folders do not exist, and the parameter createParentDirectories is false, a
        FileNotFound fault is thrown. If the intermediate level folders do not exist,
        and the parameter createParentDirectories is true, all the non-existent folders
        are created.Create a folder using the specified name. If the parent or
        intermediate level folders do not exist, and the parameter
        createParentDirectories is false, a FileNotFound fault is thrown. If the
        intermediate level folders do not exist, and the parameter
        createParentDirectories is true, all the non-existent folders are created.
        
        :param name: The name of the folder, either a URL or a datastore path referring to the folder to be created.
        
        :param datacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,must be a URL.
        
        :param createParentDirectories: If true, any non-existent intermediate level folders will be created. If not specified, it is assumed to be false.
        
        '''
        return self.delegate("MakeDirectory")(name, datacenter, createParentDirectories)
    
    def MoveDatastoreFile_Task(self, sourceName, destinationName, sourceDatacenter=None, destinationDatacenter=None, force=None):
        '''Moves the source file or folder to the destination.Moves the source file or
        folder to the destination.Moves the source file or folder to the
        destination.Moves the source file or folder to the destination.Moves the source
        file or folder to the destination.Moves the source file or folder to the
        destination.Moves the source file or folder to the destination.Moves the source
        file or folder to the destination.Moves the source file or folder to the
        destination.
        
        :param sourceName: The name of the source, either a URL or a datastore path referring to the file or folder to be moved.
        
        :param sourceDatacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,must be a URL.
        
        :param destinationName: The name of the destination, either a URL or a datastore path referring to the destination file or folder.
        
        :param destinationDatacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter, it is assumed that the destination path belongs to the source datacenter.
        
        :param force: If true, overwrite any identically named file at the destination. If not specified, it is assumed to be false.
        
        '''
        return self.delegate("MoveDatastoreFile_Task")(sourceName, sourceDatacenter, destinationName, destinationDatacenter, force)