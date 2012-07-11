
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class GuestFileManager(BaseEntity):
    '''FileManager is the managed object that provides APIs to manipulate the guest
    operating system files.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.GuestFileManager):
        super(GuestFileManager, self).__init__(core, name=name, ref=ref, type=type)

    

    
    
    def ChangeFileAttributesInGuest(self, vm, auth, guestFilePath, fileAttributes):
        '''Changes the file attributes of a specified file inside the guest.
        
        :param vm: Virtual Machine to perform the operation on.
        
        :param auth: The guest authentication data. See GuestAuthentication.
        
        :param guestFilePath: The complete path to the file to be copied in the guest. If the file points to an symbolic link, then the attributes of the target file are changed.
        
        :param fileAttributes: Specifies the different file attributes of the guest file to be changed. See GuestFileAttributes. If any property is not specified, then the specific attribute of the file will be unchanged.
        
        '''
        return self.delegate("ChangeFileAttributesInGuest")(vm, auth, guestFilePath, fileAttributes)
    
    def CreateTemporaryDirectoryInGuest(self, vm, auth, prefix, suffix, directoryPath=None):
        '''Creates a temporary directory.Creates a temporary directory.
        
        :param vm: Virtual Machine to perform the operation on.
        
        :param auth: The guest authentication data. See GuestAuthentication.
        
        :param prefix: The prefix to be given to the new temporary directory.
        
        :param suffix: The suffix to be given to the new temporary directory.
        
        :param directoryPath: The complete path to the directory in which to create the new directory. If unset or an empty string, a guest-specific location will be used.
        
        '''
        return self.delegate("CreateTemporaryDirectoryInGuest")(vm, auth, prefix, suffix, directoryPath)
    
    def CreateTemporaryFileInGuest(self, vm, auth, prefix, suffix, directoryPath=None):
        '''Creates a temporary file.Creates a temporary file.
        
        :param vm: Virtual Machine to perform the operation on.
        
        :param auth: The guest authentication data. See GuestAuthentication.
        
        :param prefix: The prefix to be given to the new temporary file.
        
        :param suffix: The suffix to be given to the new temporary file.
        
        :param directoryPath: The complete path to the directory in which to create the file. If unset, or an empty string, a guest-specific location will be used.
        
        '''
        return self.delegate("CreateTemporaryFileInGuest")(vm, auth, prefix, suffix, directoryPath)
    
    def DeleteDirectoryInGuest(self, vm, auth, directoryPath, recursive):
        '''Deletes a directory in the guest OS.
        
        :param vm: Virtual Machine to perform the operation on.
        
        :param auth: The guest authentication data. See GuestAuthentication.
        
        :param directoryPath: The complete path to the directory to be deleted.
        
        :param recursive: If true, all subdirectories are also deleted. If false, the directory must be empty for the operation to succeed.
        
        '''
        return self.delegate("DeleteDirectoryInGuest")(vm, auth, directoryPath, recursive)
    
    def DeleteFileInGuest(self, vm, auth, filePath):
        '''Deletes a file in the guest OS
        
        :param vm: Virtual Machine to perform the operation on.
        
        :param auth: The guest authentication data. See GuestAuthentication.
        
        :param filePath: The complete path to the file or symbolic link to be deleted.
        
        '''
        return self.delegate("DeleteFileInGuest")(vm, auth, filePath)
    
    def InitiateFileTransferFromGuest(self, vm, auth, guestFilePath):
        '''Initiates an operation to transfer a file from the guest.Initiates an operation
        to transfer a file from the guest.
        
        :param vm: Virtual Machine to perform the operation on.
        
        :param auth: The guest authentication data.
        
        :param guestFilePath: The complete path to the file inside the guest that has to be transferred to the client. It cannot be a path to a directory or a symbolic link.
        
        '''
        return self.delegate("InitiateFileTransferFromGuest")(vm, auth, guestFilePath)
    
    def InitiateFileTransferToGuest(self, vm, auth, guestFilePath, fileAttributes, fileSize, overwrite):
        '''Initiates an operation to transfer a file to the guest.Initiates an operation
        to transfer a file to the guest.
        
        :param vm: Virtual Machine to perform the operation on.
        
        :param auth: The guest authentication data. See GuestAuthentication.
        
        :param guestFilePath: The complete destination path in the guest to transfer the file from the client. It cannot be a path to a directory or a symbolic link.
        
        :param fileAttributes: File attributes of the file that has to be created in the guest. See GuestFileAttributes. If any file attribute is not specified, then the default value of that property will be set for the file.
        
        :param fileSize: Size of the file to transfer to the guest in bytes.
        
        :param overwrite: If set, the destination file is clobbered.
        
        '''
        return self.delegate("InitiateFileTransferToGuest")(vm, auth, guestFilePath, fileAttributes, fileSize, overwrite)
    
    def ListFilesInGuest(self, vm, auth, filePath, index=None, maxResults=None, matchPattern=None):
        '''Returns information about files or directories in the guest.Returns information
        about files or directories in the guest.
        
        :param vm: Virtual Machine to perform the operation on.
        
        :param auth: The guest authentication data. See GuestAuthentication.
        
        :param filePath: The complete path to the directory or file to query.
        
        :param index: Which result to start the list with. The default is 0.
        
        :param maxResults: The maximum number of results to return. The default is 50.
        
        :param matchPattern: A filter for the return values. Match patterns are specified using perl-compatible regular expressions. If matchPattern is unset, then the pattern '.*' is used.
        
        '''
        return self.delegate("ListFilesInGuest")(vm, auth, filePath, index, maxResults, matchPattern)
    
    def MakeDirectoryInGuest(self, vm, auth, directoryPath, createParentDirectories):
        '''Creates a directory in the guest OS
        
        :param vm: Virtual Machine to perform the operation on.
        
        :param auth: The guest authentication data. See GuestAuthentication.
        
        :param directoryPath: The complete path to the directory to be created.
        
        :param createParentDirectories: Whether any parent directories are to be created.
        
        '''
        return self.delegate("MakeDirectoryInGuest")(vm, auth, directoryPath, createParentDirectories)
    
    def MoveDirectoryInGuest(self, vm, auth, srcDirectoryPath, dstDirectoryPath):
        '''Moves or renames a directory in the guest.
        
        :param vm: Virtual Machine to perform the operation on.
        
        :param auth: The guest authentication data. See GuestAuthentication.
        
        :param srcDirectoryPath: The complete path to the directory to be moved.
        
        :param dstDirectoryPath: The complete path to the where the directory is moved or its new name. It cannot be a path to an existing directory or an existing file.
        
        '''
        return self.delegate("MoveDirectoryInGuest")(vm, auth, srcDirectoryPath, dstDirectoryPath)
    
    def MoveFileInGuest(self, vm, auth, srcFilePath, dstFilePath, overwrite):
        '''Renames a file in the guest.
        
        :param vm: Virtual Machine to perform the operation on.
        
        :param auth: The guest authentication data. See GuestAuthentication.
        
        :param srcFilePath: The complete path to the original file or symbolic link to be moved.
        
        :param dstFilePath: The complete path to the where the file is renamed. It cannot be a path to an existing diectory.
        
        :param overwrite: If set, the destination file is clobbered.
        
        '''
        return self.delegate("MoveFileInGuest")(vm, auth, srcFilePath, dstFilePath, overwrite)