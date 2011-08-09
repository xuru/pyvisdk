
from pyvisdk.do.dvs_event import DvsEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DvsRenamedEvent(DvsEvent):
    '''A distributed virtual switch was renamed.
    '''
    
    def __init__(self, newName, oldName):
        # MUST define these
        super(DvsRenamedEvent, self).__init__()
    
        self.data['newName'] = newName
        self.data['oldName'] = oldName
    
    
    @property
    def newName(self):
        '''The new DistributedVirtualSwitch name.
        '''
        return self.data['newName']

    @property
    def oldName(self):
        '''The old DistributedVirtualSwitch name.
        '''
        return self.data['oldName']

