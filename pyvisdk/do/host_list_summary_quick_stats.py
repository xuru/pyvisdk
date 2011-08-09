
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostListSummaryQuickStats(DynamicData):
    '''Basic host statistics.Included in the host statistics are fairness scores.
        Fairness scores are represented in units with relative values, meaning
        they are evaluated relative to the scores of other hosts. They should not
        be thought of as having any particular absolute value. Each fairness unit
        represents an increment of 0.001 in a fairness score. The further the
        fairness score diverges from 1, the less fair the allocation. Therefore, a
        fairness score of 990, representing 0.990, is more fair than a fairness
        score of 1015, which represents 1.015. This is because 1.015 is further
        from 1 than 0.990.
    '''
    
    def __init__(self, distributedCpuFairness, distributedMemoryFairness, overallCpuUsage, overallMemoryUsage, uptime):
        # MUST define these
        super(HostListSummaryQuickStats, self).__init__()
    
        self.data['distributedCpuFairness'] = distributedCpuFairness
        self.data['distributedMemoryFairness'] = distributedMemoryFairness
        self.data['overallCpuUsage'] = overallCpuUsage
        self.data['overallMemoryUsage'] = overallMemoryUsage
        self.data['uptime'] = uptime
    
    
    @property
    def distributedCpuFairness(self):
        '''The fairness of distributed CPU resource allocation on the host.
        '''
        return self.data['distributedCpuFairness']

    @property
    def distributedMemoryFairness(self):
        '''The fairness of distributed memory resource allocation on the host.
        '''
        return self.data['distributedMemoryFairness']

    @property
    def overallCpuUsage(self):
        '''Aggregated CPU usage across all cores on the host in MHz. This is only available
        if the host is connected.
        '''
        return self.data['overallCpuUsage']

    @property
    def overallMemoryUsage(self):
        '''Physical memory usage on the host in MB. This is only available if the host is
        connected.
        '''
        return self.data['overallMemoryUsage']

    @property
    def uptime(self):
        '''The system uptime of the host in seconds.
        '''
        return self.data['uptime']

