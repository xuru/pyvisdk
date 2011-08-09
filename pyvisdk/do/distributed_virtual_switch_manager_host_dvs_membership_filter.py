
from pyvisdk.do.distributed_virtual_switch_manager_host_dvs_filter_spec import DistributedVirtualSwitchManagerHostDvsFilterSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitchManagerHostDvsMembershipFilter(DistributedVirtualSwitchManagerHostDvsFilterSpec):
    '''Check host compatibility against all hosts in the DVS (or not in the DVS if
        inclusive flag in base class is false)
    '''
    
    def __init__(self, distributedVirtualSwitch):
        # MUST define these
        super(DistributedVirtualSwitchManagerHostDvsMembershipFilter, self).__init__()
    
        self.data['distributedVirtualSwitch'] = distributedVirtualSwitch
    
    
    @property
    def distributedVirtualSwitch(self):
        '''
        '''
        return self.data['distributedVirtualSwitch']

