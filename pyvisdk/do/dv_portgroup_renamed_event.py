
from pyvisdk.do.dv_portgroup_event import DVPortgroupEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVPortgroupRenamedEvent(DVPortgroupEvent):
    '''Two distributed virtual portgroup was renamed.
    '''
    
    def __init__(self, newName, oldName):
        # MUST define these
        super(DVPortgroupRenamedEvent, self).__init__()
    
        self.data['newName'] = newName
        self.data['oldName'] = oldName
    
    
    @property
    def newName(self):
        '''The new portgroup name.
        '''
        return self.data['newName']

    @property
    def oldName(self):
        '''The old portgroup name.
        '''
        return self.data['oldName']

