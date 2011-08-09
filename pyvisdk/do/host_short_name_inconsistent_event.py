
from pyvisdk.do.host_das_event import HostDasEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostShortNameInconsistentEvent(HostDasEvent):
    '''This event records that host name resolution returned different names on the host.
        Please check your host's network configuration and your DNS configuration.
        There may be duplicate entries.
    '''
    
    def __init__(self, shortName, shortName2):
        # MUST define these
        super(HostShortNameInconsistentEvent, self).__init__()
    
        self.data['shortName'] = shortName
        self.data['shortName2'] = shortName2
    
    
    @property
    def shortName(self):
        '''
        '''
        return self.data['shortName']

    @property
    def shortName2(self):
        '''
        '''
        return self.data['shortName2']

