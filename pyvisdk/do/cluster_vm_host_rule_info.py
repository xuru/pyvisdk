
from pyvisdk.do.cluster_rule_info import ClusterRuleInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterVmHostRuleInfo(ClusterRuleInfo):
    '''A ClusterVmHostRuleInfo object identifies virtual machines and host groups that
        determine virtual machine placement. The virtual machines and hosts
        referenced by a VM-Host rule must be in the same cluster.A VM-Host rule
        identifies the following groups.* A virtual machine group
        (ClusterVmGroup). * Two host groups - an affine host group and an anti-
        affine host group (ClusterHostGroup). At least one of the groups must
        contain one or more hosts.ClusterVmHostRuleInfo stores only the names of
        the relevant virtual machine and host groups. The group contents are
        stored in the virtual machine and host group objects.When you modify a VM-
        Host rule, only the fields that are specified are set.
    '''
    
    def __init__(self, affineHostGroupName, antiAffineHostGroupName, vmGroupName):
        # MUST define these
        super(ClusterVmHostRuleInfo, self).__init__()
    
        self.data['affineHostGroupName'] = affineHostGroupName
        self.data['antiAffineHostGroupName'] = antiAffineHostGroupName
        self.data['vmGroupName'] = vmGroupName
    
    
    @property
    def affineHostGroupName(self):
        '''Name of the affine host group (ClusterHostGroup.name). The affine host group
        identifies hosts on which vmGroupName virtual machines can be powered-on.
        The value of the mandatory property determines how the Server interprets
        the rule.
        '''
        return self.data['affineHostGroupName']

    @property
    def antiAffineHostGroupName(self):
        '''Name of the anti-affine host group (ClusterHostGroup.name). The anti-affine host
        group identifies hosts on which vmGroupName virtual machines should not be
        powered-on. The value of the mandatory property determines how the Server
        interprets the rule.
        '''
        return self.data['antiAffineHostGroupName']

    @property
    def vmGroupName(self):
        '''Virtual group name (ClusterVmGroup.name). The virtual group may contain one or
        more virtual machines.
        '''
        return self.data['vmGroupName']

