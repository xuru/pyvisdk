
from pyvisdk.do.dvs_uplink_port_policy import DVSUplinkPortPolicy
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVSNameArrayUplinkPortPolicy(DVSUplinkPortPolicy):
    '''The uplink port policy specifies an array of uniform names for the uplink ports
        across the hosts. The size of the array indicates the number of uplink
        ports that will be created for each host in the switch.When the names in
        this array change, the uplink ports on all the hosts are automatically
        renamed accordingly. Increasing the number of names in the array
        automatically creates additional uplink ports bearing the added name on
        each host. Decreasing the number of name automatically deletes the unused
        uplink ports on each host. Decreasing beyond the number of unused uplink
        port raises a fault.This policy overrides the portgroup's port naming
        format, if both are defined and the uplink ports are created in a uplink
        portgroup.
    '''
    
    def __init__(self, uplinkPortName):
        # MUST define these
        super(DVSNameArrayUplinkPortPolicy, self).__init__()
    
        self.data['uplinkPortName'] = uplinkPortName
    
    
    @property
    def uplinkPortName(self):
        '''The uniform name of uplink ports on each host.
        '''
        return self.data['uplinkPortName']

