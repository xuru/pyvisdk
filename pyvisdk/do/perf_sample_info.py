
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PerfSampleInfo(DynamicData):
    '''This data object type describes information contained in a sample collection, its
        timestamp, and sampling interval.
    '''
    
    def __init__(self, interval, timestamp):
        # MUST define these
        super(PerfSampleInfo, self).__init__()
    
        self.data['interval'] = interval
        self.data['timestamp'] = timestamp
    
    
    @property
    def interval(self):
        '''The interval in seconds for which performance statistics were collected. This can
        be the refreshRate of the managed object for which this statistics was
        collected or one of the intervals for historical statistics configured in
        the system. See UpdatePerfInterval for more information about the
        intervals configured in the system.
        '''
        return self.data['interval']

    @property
    def timestamp(self):
        '''The time at which the sample was collected.
        '''
        return self.data['timestamp']

