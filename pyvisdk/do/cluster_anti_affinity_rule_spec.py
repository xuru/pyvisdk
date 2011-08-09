
from pyvisdk.do.cluster_rule_info import ClusterRuleInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterAntiAffinityRuleSpec(ClusterRuleInfo):
    '''The ClusterAntiAffinityRuleSpec data object defines a set of virtual machines. DRS
        will attempt to schedule the virtual machines to run on different hosts.
    '''
    
    def __init__(self, vm):
        # MUST define these
        super(ClusterAntiAffinityRuleSpec, self).__init__()
    
        self.data['vm'] = vm
    
    
    @property
    def vm(self):
        '''List of virtual machine references.
        '''
        return self.data['vm']

