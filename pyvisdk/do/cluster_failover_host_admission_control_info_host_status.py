
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterFailoverHostAdmissionControlInfoHostStatus(DynamicData):
    '''Data object containing the status of a failover host.
    '''
    
    def __init__(self, host, status):
        # MUST define these
        super(ClusterFailoverHostAdmissionControlInfoHostStatus, self).__init__()
    
        self.data['host'] = host
        self.data['status'] = status
    
    
    @property
    def host(self):
        '''The failover host.
        '''
        return self.data['host']

    @property
    def status(self):
        '''The status of the failover host. The status is green for a connected host with no
        VMware HA errors and no virtual machines running on it. The status is
        yellow for a connected host with no VMware HA errors and some virtual
        machines running on it. The status red for a disconnected or not
        responding host, a host that is in maintenance or standby mode or that has
        a VMware HA error on it.
        '''
        return self.data['status']

