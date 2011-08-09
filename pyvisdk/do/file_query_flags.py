
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class FileQueryFlags(DynamicData):
    '''The FileInfo.Details data object type is a set of flags for a search request. This
        search request specifies which details to return for each matching file.
        This data object type is here to ensure that there is one flag
        corresponding to each FileInfo property other than the path name, which a
        search always returns.
    '''
    
    def __init__(self, fileOwner, fileSize, fileType, modification):
        # MUST define these
        super(FileQueryFlags, self).__init__()
    
        self.data['fileOwner'] = fileOwner
        self.data['fileSize'] = fileSize
        self.data['fileType'] = fileType
        self.data['modification'] = modification
    
    
    @property
    def fileOwner(self):
        '''The flag to indicate whether or not to return the file owner.
        '''
        return self.data['fileOwner']

    @property
    def fileSize(self):
        '''The flag to indicate whether or not the size of the file is returned.
        '''
        return self.data['fileSize']

    @property
    def fileType(self):
        '''The flag to indicate whether or not the files that match this query specification
        are returned along with file type information. This field must be set to
        return specific details about the file type.
        '''
        return self.data['fileType']

    @property
    def modification(self):
        '''The flag to indicate whether or not to return the date and time the file was last
        modified.
        '''
        return self.data['modification']

