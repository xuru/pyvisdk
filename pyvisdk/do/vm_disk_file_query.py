
from pyvisdk.do.file_query import FileQuery
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmDiskFileQuery(FileQuery):
    '''This data object type describes the query specification for the virtual disk
        primary file.
    '''
    
    def __init__(self, details, filter):
        # MUST define these
        super(VmDiskFileQuery, self).__init__()
    
        self.data['details'] = details
        self.data['filter'] = filter
    
    
    @property
    def details(self):
        '''Details specification for the virtual disk primary file query.
        '''
        return self.data['details']

    @property
    def filter(self):
        '''The filter specification for the virtual disk primary file query.
        '''
        return self.data['filter']

