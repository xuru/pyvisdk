
from pyvisdk.do.dvs_event import DvsEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DvsMergedEvent(DvsEvent):
    '''Two distributed virtual switches was merged.
    '''
    
    def __init__(self, destinationDvs, sourceDvs):
        # MUST define these
        super(DvsMergedEvent, self).__init__()
    
        self.data['destinationDvs'] = destinationDvs
        self.data['sourceDvs'] = sourceDvs
    
    
    @property
    def destinationDvs(self):
        '''The destination DVS.
        '''
        return self.data['destinationDvs']

    @property
    def sourceDvs(self):
        '''The source DVS.
        '''
        return self.data['sourceDvs']

