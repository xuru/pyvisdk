
from pyvisdk.do.cluster_group_info import ClusterGroupInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterVmGroup(ClusterGroupInfo):
    '''The ClusterVmGroup data object identifies virtual machines for VM-Host rules. VM-
        Host rules determine placement of virtual machines on hosts in a cluster.
        The logic specified in a ClusterVmHostRuleInfo object determines where
        virtual machines can be powered-on.If a virtual machine is removed from
        the cluster, it loses its DRS group affiliation. The Server does not
        restore any group affiliations if the virtual machine is returned to the
        cluster.
    '''
    
    def __init__(self, vm):
        # MUST define these
        super(ClusterVmGroup, self).__init__()
    
        self.data['vm'] = vm
    
    
    @property
    def vm(self):
        '''List of virtual machines that are part of this group. A virtual machine group can
        contain zero or more virtual machines.
        '''
        return self.data['vm']

