
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ModeInfo(DynamicData):
    '''The FileAccess.Modes data object type defines the known access modes for a
        datastore. The property values specify how to interpret the "what"
        property for a FileAccess object.
    '''
    
    def __init__(self, admin, browse, full, modify, read, use):
        # MUST define these
        super(ModeInfo, self).__init__()
    
        self.data['admin'] = admin
        self.data['browse'] = browse
        self.data['full'] = full
        self.data['modify'] = modify
        self.data['read'] = read
        self.data['use'] = use
    
    
    @property
    def admin(self):
        '''Can change permissions for a file.
        '''
        return self.data['admin']

    @property
    def browse(self):
        '''Can see the existence of a file.
        '''
        return self.data['browse']

    @property
    def full(self):
        '''Can do anything to a file, including change permissions.
        '''
        return self.data['full']

    @property
    def modify(self):
        '''Can read and write a file.
        '''
        return self.data['modify']

    @property
    def read(self):
        '''Can read a file.
        '''
        return self.data['read']

    @property
    def use(self):
        '''Can execute or operate a file or look inside a directory.
        '''
        return self.data['use']

