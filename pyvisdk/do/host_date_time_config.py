
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDateTimeConfig(DynamicData):
    '''This data object represents the dateTime configuration of the host.
    '''
    
    def __init__(self, ntpConfig, timeZone):
        # MUST define these
        super(HostDateTimeConfig, self).__init__()
    
        self.data['ntpConfig'] = ntpConfig
        self.data['timeZone'] = timeZone
    
    
    @property
    def ntpConfig(self):
        '''The NTP configuration on the host.
        '''
        return self.data['ntpConfig']

    @property
    def timeZone(self):
        '''The time zone of the host. Must be one of the values of key
        '''
        return self.data['timeZone']

