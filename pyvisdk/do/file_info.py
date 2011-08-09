
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class FileInfo(DynamicData):
    '''This data object type contains rudimentary information about a file in a
        datastore. The information here is not meant to cover all information in
        traditional file systems, but rather to provide sufficient information for
        files that are associated with virtual machines. Derived types describe
        the known file types for a datastore.
    '''
    
    def __init__(self, fileSize, modification, owner, path):
        # MUST define these
        super(FileInfo, self).__init__()
    
        self.data['fileSize'] = fileSize
        self.data['modification'] = modification
        self.data['owner'] = owner
        self.data['path'] = path
    
    
    @property
    def fileSize(self):
        '''The size of the file in bytes.
        '''
        return self.data['fileSize']

    @property
    def modification(self):
        '''The last date and time the file was modified.
        '''
        return self.data['modification']

    @property
    def owner(self):
        '''The user name of the owner of the file.
        '''
        return self.data['owner']

    @property
    def path(self):
        '''The path relative to the folder path in the search results.
        '''
        return self.data['path']

