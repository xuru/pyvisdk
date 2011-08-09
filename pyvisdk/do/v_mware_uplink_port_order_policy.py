
from pyvisdk.do.inheritable_policy import InheritablePolicy
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VMwareUplinkPortOrderPolicy(InheritablePolicy):
    '''This data object type describes uplink port ordering policy for a distributed
        virtual port. A uplink port can be in the active list, the standby list,
        or neither. It cannot be in both lists.
    '''
    
    def __init__(self, activeUplinkPort, standbyUplinkPort):
        # MUST define these
        super(VMwareUplinkPortOrderPolicy, self).__init__()
    
        self.data['activeUplinkPort'] = activeUplinkPort
        self.data['standbyUplinkPort'] = standbyUplinkPort
    
    
    @property
    def activeUplinkPort(self):
        '''List of active uplink ports used for load balancing.
        '''
        return self.data['activeUplinkPort']

    @property
    def standbyUplinkPort(self):
        '''Standby uplink ports used for failover.
        '''
        return self.data['standbyUplinkPort']

