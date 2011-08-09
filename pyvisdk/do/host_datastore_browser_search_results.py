
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDatastoreBrowserSearchResults(DynamicData):
    '''This data object type contains the results of a search method for one datastore. A
        search method typically returns a set of these objects as an array.
    '''
    
    def __init__(self, datastore, file, folderPath):
        # MUST define these
        super(HostDatastoreBrowserSearchResults, self).__init__()
    
        self.data['datastore'] = datastore
        self.data['file'] = file
        self.data['folderPath'] = folderPath
    
    
    @property
    def datastore(self):
        '''Datastore contains the results.
        '''
        return self.data['datastore']

    @property
    def file(self):
        '''Set of matching files, if any.
        '''
        return self.data['file']

    @property
    def folderPath(self):
        '''Relative path to the top-level folder.
        '''
        return self.data['folderPath']

