
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineAffinityInfo(DynamicData):
    '''Specification of scheduling affinity.Scheduling affinity is used for explicitly
        specifying which processors or NUMA nodes may be used by a virtual
        machine.
    '''
    
    def __init__(self, affinitySet):
        # MUST define these
        super(VirtualMachineAffinityInfo, self).__init__()
    
        self.data['affinitySet'] = affinitySet
    
    
    @property
    def affinitySet(self):
        '''List of nodes (processors for CPU, NUMA nodes for memory) that may be used by the
        virtual machine. If the array is empty when modifying the affinity
        setting, then any existing affinity is removed.
        '''
        return self.data['affinitySet']

