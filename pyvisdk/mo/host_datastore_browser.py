
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDatastoreBrowser(BaseEntity):
    '''The DatastoreBrowser managed object type provides access to the contents of one or
        more datastores. The items in a datastore are files that contain
        configuration, virtual disk, and the other data associated with a virtual
        machine.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostDatastoreBrowser):
        # MUST define these
        super(HostDatastoreBrowser, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def datastore(self):
        '''
        Set of datastores that can be searched on this DatastoreBrowser.
        '''
        return self.update('datastore')

    @property
    def supportedType(self):
        '''
        The list of supported file types. The supported file types are represented as
        items in this list. For each supported file type, there is an object in
        the list whose dynamic type is one of the types derived from the FileQuery
        data object type. In general, the properties in this query type are not
        set.
        '''
        return self.update('supportedType')


    def SearchDatastoreSubFolders_Task(self, datastorePath):
        '''Returns the information for the files that match the given search criteria as a
        SearchResults[] object. Searches the folder specified by the datastore
        path and all subfolders. The Datastore.Browse privilege must be held on
        the datastore identified by the datastore path.

        :param datastorePath: 


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("SearchDatastoreSubFolders_Task")(datastorePath)
        

    def DeleteFile(self, datastorePath):
        '''Deprecated. As of VI API 2.5, use DeleteDatastoreFile_Task. Deletes the specified
        files from the datastore. If a valid virtual disk file is specified, then
        all the components of the virtual disk are deleted.

        :param datastorePath: 

        '''
        
        return self.delegate("DeleteFile")(datastorePath)
        

    def SearchDatastore_Task(self, datastorePath):
        '''Returns the information for the files that match the given search criteria as a
        SearchResults object. Searches only the folder specified by the datastore
        path. The Datastore.Browse privilege must be held on the datastore
        identified by the datastore path.

        :param datastorePath: 


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("SearchDatastore_Task")(datastorePath)
        
