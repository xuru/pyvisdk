
from pyvisdk.do.cluster_das_advanced_runtime_info import ClusterDasAdvancedRuntimeInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterDasFailoverLevelAdvancedRuntimeInfo(ClusterDasAdvancedRuntimeInfo):
    '''Advanced runtime information related to the high availability service for a
        cluster that has been configured with a failover level admission control
        policy. See ClusterFailoverLevelAdmissionControlPolicy.
    '''
    
    def __init__(self, hostSlots, slotInfo, totalGoodHosts, totalHosts, totalSlots, totalVms, unreservedSlots, usedSlots):
        # MUST define these
        super(ClusterDasFailoverLevelAdvancedRuntimeInfo, self).__init__()
    
        self.data['hostSlots'] = hostSlots
        self.data['slotInfo'] = slotInfo
        self.data['totalGoodHosts'] = totalGoodHosts
        self.data['totalHosts'] = totalHosts
        self.data['totalSlots'] = totalSlots
        self.data['totalVms'] = totalVms
        self.data['unreservedSlots'] = unreservedSlots
        self.data['usedSlots'] = usedSlots
    
    
    @property
    def hostSlots(self):
        '''
        '''
        return self.data['hostSlots']

    @property
    def slotInfo(self):
        '''Slot information for this cluster.
        '''
        return self.data['slotInfo']

    @property
    def totalGoodHosts(self):
        '''The total number of connected hosts that are not in maintance mode and that do not
        have any DAS-related config issues on them.
        '''
        return self.data['totalGoodHosts']

    @property
    def totalHosts(self):
        '''The total number of hosts in the cluster.
        '''
        return self.data['totalHosts']

    @property
    def totalSlots(self):
        '''The total number of slots available in the cluster.
        '''
        return self.data['totalSlots']

    @property
    def totalVms(self):
        '''The total number of powered on vms in the cluster.
        '''
        return self.data['totalVms']

    @property
    def unreservedSlots(self):
        '''The number of slots that are not used by currently powered on virtual machines and
        not reserved to satisfy the configured failover level. This number gives
        an indication of how many additional virtual machines can be powered on in
        this cluster without violating the failover level (assuming the new
        virtual machine's reservations are satisfied by the current slot size).
        This value is computed as follows (where m is the configured failover
        level): Remove the m largest hosts (ie. the ones with the most slots) from
        the list of "good" hosts (see totalGoodHosts). Sum up the number of slots
        on the remaining hosts and deduct the number of currently used slots (see
        usedSlots). If this number is negative, use zero instead.
        '''
        return self.data['unreservedSlots']

    @property
    def usedSlots(self):
        '''The number of slots currently being used.
        '''
        return self.data['usedSlots']

