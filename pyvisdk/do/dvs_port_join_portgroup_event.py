
from pyvisdk.do.dvs_event import DvsEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DvsPortJoinPortgroupEvent(DvsEvent):
    '''A port was moved into the distributed virtual portgroup.
    '''
    
    def __init__(self, portgroupKey, portgroupName, portKey):
        # MUST define these
        super(DvsPortJoinPortgroupEvent, self).__init__()
    
        self.data['portgroupKey'] = portgroupKey
        self.data['portgroupName'] = portgroupName
        self.data['portKey'] = portKey
    
    
    @property
    def portgroupKey(self):
        '''The portgroup key.
        '''
        return self.data['portgroupKey']

    @property
    def portgroupName(self):
        '''The portgroup name.
        '''
        return self.data['portgroupName']

    @property
    def portKey(self):
        '''The port key.
        '''
        return self.data['portKey']

