
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNicOrderPolicy(DynamicData):
    '''This data object type describes network adapter ordering policy for a network
        adapter team. A physical network adapter can be in the active list, the
        standby list, or neither. It cannot be in both lists. For a virtual
        switch, the NicOrderPolicy property is never null when retrieved from the
        server. When creating a new virtual switch or updating an existing virtual
        switch, the NicOrderPolicy can be null, in which case the default
        NicOrderPolicy from the server will be used. For a portgroup, a null
        NicOrderPolicy property means the portgroup inherits the policy from its
        parent. Otherwise, the NicOrderPolicy property defined in the portgroup
        takes precedence. In all cases where the NicOrderPolicy property is set,
        an empty activeNic array means there are no active Ethernet adapters in
        the team. An empty standbyNic array means there are no standby Ethernet
        adapters.
    '''
    
    def __init__(self, activeNic, standbyNic):
        # MUST define these
        super(HostNicOrderPolicy, self).__init__()
    
        self.data['activeNic'] = activeNic
        self.data['standbyNic'] = standbyNic
    
    
    @property
    def activeNic(self):
        '''List of active network adapters used for load balancing.
        '''
        return self.data['activeNic']

    @property
    def standbyNic(self):
        '''Standby network adapters used for failover.
        '''
        return self.data['standbyNic']

