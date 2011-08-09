
from pyvisdk.do.datacenter_event import DatacenterEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DatacenterRenamedEvent(DatacenterEvent):
    '''
    '''
    
    def __init__(self, newName, oldName):
        # MUST define these
        super(DatacenterRenamedEvent, self).__init__()
    
        self.data['newName'] = newName
        self.data['oldName'] = oldName
    
    
    @property
    def newName(self):
        '''The new datacenter name.
        '''
        return self.data['newName']

    @property
    def oldName(self):
        '''The old datacenter name.
        '''
        return self.data['oldName']

