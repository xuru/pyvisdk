
from pyvisdk.do.cluster_group_info import ClusterGroupInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterHostGroup(ClusterGroupInfo):
    '''The ClusterHostGroup data object identifies hosts for VM-Host rules. VM-Host rules
        determine placement of virtual machines on hosts in a cluster. The logic
        specified in a ClusterVmHostRuleInfo object determines where virtual
        machines can be powered-on.
    '''
    
    def __init__(self, host):
        # MUST define these
        super(ClusterHostGroup, self).__init__()
    
        self.data['host'] = host
    
    
    @property
    def host(self):
        '''List of hosts that are part of this group. A host group can contain zero or more
        hosts.
        '''
        return self.data['host']

