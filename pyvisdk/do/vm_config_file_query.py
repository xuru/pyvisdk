
from pyvisdk.do.file_query import FileQuery
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmConfigFileQuery(FileQuery):
    '''This data object type describes query specification for the virtual machine
        configuration file.
    '''
    
    def __init__(self, details, filter):
        # MUST define these
        super(VmConfigFileQuery, self).__init__()
    
        self.data['details'] = details
        self.data['filter'] = filter
    
    
    @property
    def details(self):
        '''The details specification for the virtual machine configuration file query.
        '''
        return self.data['details']

    @property
    def filter(self):
        '''The filter specification for the virtual machine configuration file query.
        '''
        return self.data['filter']

