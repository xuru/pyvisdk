
from pyvisdk.do.inheritable_policy import InheritablePolicy
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVSFailureCriteria(InheritablePolicy):
    '''This data object type describes the network adapter failover detection algorithm
        for a network adapter team.
    '''
    
    def __init__(self, checkBeacon, checkDuplex, checkErrorPercent, checkSpeed, fullDuplex, percentage, speed):
        # MUST define these
        super(DVSFailureCriteria, self).__init__()
    
        self.data['checkBeacon'] = checkBeacon
        self.data['checkDuplex'] = checkDuplex
        self.data['checkErrorPercent'] = checkErrorPercent
        self.data['checkSpeed'] = checkSpeed
        self.data['fullDuplex'] = fullDuplex
        self.data['percentage'] = percentage
        self.data['speed'] = speed
    
    
    @property
    def checkBeacon(self):
        '''The flag to indicate whether or not to enable this property to enable beacon
        probing as a method to validate the link status of a physical network
        adapter.
        '''
        return self.data['checkBeacon']

    @property
    def checkDuplex(self):
        '''The flag to indicate whether or not to use the link duplex reported by the driver
        as link selection criteria.
        '''
        return self.data['checkDuplex']

    @property
    def checkErrorPercent(self):
        '''The flag to indicate whether or not to use link error percentage to detect
        failure.
        '''
        return self.data['checkErrorPercent']

    @property
    def checkSpeed(self):
        '''To use link speed as the criteria,
        '''
        return self.data['checkSpeed']

    @property
    def fullDuplex(self):
        '''See checkDuplex
        '''
        return self.data['fullDuplex']

    @property
    def percentage(self):
        '''See checkErrorPercent
        '''
        return self.data['percentage']

    @property
    def speed(self):
        '''See checkSpeed
        '''
        return self.data['speed']

