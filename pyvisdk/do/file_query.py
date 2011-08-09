
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class FileQuery(DynamicData):
    '''The data object type that describes the base query specification. Contains query
        filters and details that apply to every file. Querying only file details
        generally does not require opening files and so is an efficient query.
        Derived types add query parameters specific to the type of file.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(FileQuery, self).__init__()
    

    
    
