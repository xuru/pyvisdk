
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDatastoreBrowser(BaseEntity):
    '''Although datastores may often be implemented using a traditional file system, a
        full interface to a file system is not provided here. Instead, specialized
        access for virtual machine files is provided. A datastore implementation
        may completely hide the file directory structure.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostDatastoreBrowser):
        # MUST define these
        super(HostDatastoreBrowser, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def datastore(self):
        '''Set of datastores that can be searched on this DatastoreBrowser.
        '''
        return self.update('datastore')

    @property
    def supportedType(self):
        '''The list of supported file types. The supported file types are represented as
        items in this list. For each supported file type, there is an object in
        the list whose dynamic type is one of the types derived from the FileQuery
        data object type. In general, the properties in this query type are not
        set.
        '''
        return self.update('supportedType')


    def DeleteFile(self):
        '''Deprecated. As of VI API 2.5, use DeleteDatastoreFile_Task. Deletes the specified
        files from the datastore. If a valid virtual disk file is specified, then
        all the components of the virtual disk are deleted.
        '''
        
        return self.delegate("DeleteFile")()
        

    def SearchDatastore_Task(self):
        '''Returns the information for the files that match the given search criteria as a
        SearchResults object. Searches only the folder specified by the datastore
        path. The Datastore.Browse privilege must be held on the datastore
        identified by the datastore path.

        :rtype: Task 

        '''
        
        return self.delegate("SearchDatastore_Task")()
        

    def SearchDatastoreSubFolders_Task(self):
        '''Returns the information for the files that match the given search criteria as a
        SearchResults[] object. Searches the folder specified by the datastore
        path and all subfolders. The Datastore.Browse privilege must be held on
        the datastore identified by the datastore path.

        :rtype: Task 

        '''
        
        return self.delegate("SearchDatastoreSubFolders_Task")()
        
