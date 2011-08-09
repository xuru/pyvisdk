
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDatastoreBrowserSearchSpec(DynamicData):
    '''The data object type describes a search for files in one or more datastores. The
        properties do not include the starting datastore path because that path is
        a separate parameter to the search method.A SearchSpec contains the query
        parameters and some global search modifiers.
    '''
    
    def __init__(self, details, matchPattern, query, searchCaseInsensitive, sortFoldersFirst):
        # MUST define these
        super(HostDatastoreBrowserSearchSpec, self).__init__()
    
        self.data['details'] = details
        self.data['matchPattern'] = matchPattern
        self.data['query'] = query
        self.data['searchCaseInsensitive'] = searchCaseInsensitive
        self.data['sortFoldersFirst'] = sortFoldersFirst
    
    
    @property
    def details(self):
        '''This object comprises a set of booleans that describe what details to return for
        each file. The file level details apply globally to all matched files.
        '''
        return self.data['details']

    @property
    def matchPattern(self):
        '''Specifies a list of file patterns that must match for a file to be returned. This
        search property is a filter that applies globally so that only files
        matching the specified patterns are returned, regardless of the other
        search parameters.
        '''
        return self.data['matchPattern']

    @property
    def query(self):
        '''The set of file types to match, search criteria specific to the file type, and the
        amount of detail for a file. These search parameters are specific to a
        file type, meaning that they can be specified only if the file type to
        which they are associated is in the set. A file type cannot appear more
        than once in the set.
        '''
        return self.data['query']

    @property
    def searchCaseInsensitive(self):
        '''This flag indicates whether or not to search using a case insensitive match on
        type. In general the algorithm used to match file types relies on file
        extensions. Although the specific file extensions used are encapsulated by
        this API, clients are still allowed to modify the filtering behavior.
        '''
        return self.data['searchCaseInsensitive']

    @property
    def sortFoldersFirst(self):
        '''By default, files are sorted in alphabetical order regardless of file type. If
        this flag is set to "true", folders are placed at the start of the list of
        results in alphabetical order. The remaining files follow in alphabetical
        order.
        '''
        return self.data['sortFoldersFirst']

