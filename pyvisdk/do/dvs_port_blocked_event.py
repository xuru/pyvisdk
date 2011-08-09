
from pyvisdk.do.dvs_event import DvsEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DvsPortBlockedEvent(DvsEvent):
    '''A port is blocked in the distributed virtual switch.
    '''
    
    def __init__(self, portKey, statusDetail):
        # MUST define these
        super(DvsPortBlockedEvent, self).__init__()
    
        self.data['portKey'] = portKey
        self.data['statusDetail'] = statusDetail
    
    
    @property
    def portKey(self):
        '''The port key.
        '''
        return self.data['portKey']

    @property
    def statusDetail(self):
        '''Reason for port's current status
        '''
        return self.data['statusDetail']

