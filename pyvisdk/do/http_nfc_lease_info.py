
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HttpNfcLeaseInfo(DynamicData):
    '''This class holds information about the lease, such as the entity covered by the
        lease, and HTTP URLs for up/downloading file backings.
    '''
    
    def __init__(self, deviceUrl, entity, hostMap, lease, leaseTimeout, totalDiskCapacityInKB):
        # MUST define these
        super(HttpNfcLeaseInfo, self).__init__()
    
        self.data['deviceUrl'] = deviceUrl
        self.data['entity'] = entity
        self.data['hostMap'] = hostMap
        self.data['lease'] = lease
        self.data['leaseTimeout'] = leaseTimeout
        self.data['totalDiskCapacityInKB'] = totalDiskCapacityInKB
    
    
    @property
    def deviceUrl(self):
        '''The deviceUrl property contains a mapping from logical device keys to URLs.
        '''
        return self.data['deviceUrl']

    @property
    def entity(self):
        '''The VirtualMachine or VirtualApp this lease covers.
        '''
        return self.data['entity']

    @property
    def hostMap(self):
        '''Map of URLs for leased hosts for a given datastore. This is used to look up multi-
        POST-capable hosts for a datastore.
        '''
        return self.data['hostMap']

    @property
    def lease(self):
        '''The HttpNfcLease object this information belongs to.
        '''
        return self.data['lease']

    @property
    def leaseTimeout(self):
        '''Number of seconds before the lease times out. The client extends the lease by
        calling HttpNfcLeaseProgress before the timeout has expired.
        '''
        return self.data['leaseTimeout']

    @property
    def totalDiskCapacityInKB(self):
        '''Total capacity in kilobytes of all disks in all Virtual Machines covered by this
        lease. This can be used to track progress when transferring disks.
        '''
        return self.data['totalDiskCapacityInKB']

