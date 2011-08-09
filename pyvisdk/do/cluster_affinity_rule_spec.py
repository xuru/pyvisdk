
from pyvisdk.do.cluster_rule_info import ClusterRuleInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterAffinityRuleSpec(ClusterRuleInfo):
    '''The ClusterAffinityRuleSpec data object defines a set of virtual machines. DRS
        will attempt to schedule the virtual machines to run on the same host.
    '''
    
    def __init__(self, vm):
        # MUST define these
        super(ClusterAffinityRuleSpec, self).__init__()
    
        self.data['vm'] = vm
    
    
    @property
    def vm(self):
        '''List of virtual machine references.
        '''
        return self.data['vm']

