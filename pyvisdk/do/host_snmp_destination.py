
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostSnmpDestination(DynamicData):
    '''Defines a receiver for SNMP Notifications
    '''
    
    def __init__(self, community, hostName, port):
        # MUST define these
        super(HostSnmpDestination, self).__init__()
    
        self.data['community'] = community
        self.data['hostName'] = hostName
        self.data['port'] = port
    
    
    @property
    def community(self):
        '''
        '''
        return self.data['community']

    @property
    def hostName(self):
        '''A system listening for SNMP notifications. These must be a IPv4 unicast address or
        resolvable dns name.
        '''
        return self.data['hostName']

    @property
    def port(self):
        '''UDP port to Notification receiver is listening on. udp/162 is the reserved port
        '''
        return self.data['port']

