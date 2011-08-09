
from pyvisdk.do.entity_event_argument import EntityEventArgument
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class FolderEventArgument(EntityEventArgument):
    '''The event argument is a Folder object.
    '''
    
    def __init__(self, folder):
        # MUST define these
        super(FolderEventArgument, self).__init__()
    
        self.data['folder'] = folder
    
    
    @property
    def folder(self):
        '''The Folder object.
        '''
        return self.data['folder']

