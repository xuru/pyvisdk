
from pyvisdk.do.distributed_virtual_switch_manager_host_dvs_filter_spec import DistributedVirtualSwitchManagerHostDvsFilterSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitchManagerHostContainerFilter(DistributedVirtualSwitchManagerHostDvsFilterSpec):
    '''Check host compatibility against all hosts in this
        DistributedVirtualSwitchManagerHostContainer
    '''
    
    def __init__(self, hostContainer):
        # MUST define these
        super(DistributedVirtualSwitchManagerHostContainerFilter, self).__init__()
    
        self.data['hostContainer'] = hostContainer
    
    
    @property
    def hostContainer(self):
        '''Container of hosts that are part of the filter.
        '''
        return self.data['hostContainer']

