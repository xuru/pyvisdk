
from pyvisdk.do.distributed_virtual_switch_manager_host_dvs_filter_spec import DistributedVirtualSwitchManagerHostDvsFilterSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitchManagerHostArrayFilter(DistributedVirtualSwitchManagerHostDvsFilterSpec):
    '''Check host compatibility against all hosts specified in the array.
    '''
    
    def __init__(self, host):
        # MUST define these
        super(DistributedVirtualSwitchManagerHostArrayFilter, self).__init__()
    
        self.data['host'] = host
    
    
    @property
    def host(self):
        '''List of hosts to consider.
        '''
        return self.data['host']

