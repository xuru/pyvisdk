
from pyvisdk.do.dvs_event import DvsEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DvsPortDisconnectedEvent(DvsEvent):
    '''A port is disconnected in the distributed virtual switch.
    '''
    
    def __init__(self, connectee, portKey):
        # MUST define these
        super(DvsPortDisconnectedEvent, self).__init__()
    
        self.data['connectee'] = connectee
        self.data['portKey'] = portKey
    
    
    @property
    def connectee(self):
        '''The port's formal connectee.
        '''
        return self.data['connectee']

    @property
    def portKey(self):
        '''The port key.
        '''
        return self.data['portKey']

