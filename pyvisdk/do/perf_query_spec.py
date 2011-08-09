
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PerfQuerySpec(DynamicData):
    '''This data object specifies the query parameters, including the managed object
        reference to the target entity for statistics retrieval.* If the optional
        intervalId is omitted, the metrics are returned in their originally
        sampled interval. * When an intervalId is specified, the server tries to
        summarize the information for the specified intervalId. However, if that
        interval does not exist or has no data, the server summarizes the
        information using the best interval available. * If the range between
        startTime and endTime crosses multiple sample interval periods, the result
        contains data from the longest interval in the period.
    '''
    
    def __init__(self, endTime, entity, format, intervalId, maxSample, metricId, startTime):
        # MUST define these
        super(PerfQuerySpec, self).__init__()
    
        self.data['endTime'] = endTime
        self.data['entity'] = entity
        self.data['format'] = format
        self.data['intervalId'] = intervalId
        self.data['maxSample'] = maxSample
        self.data['metricId'] = metricId
        self.data['startTime'] = startTime
    
    
    @property
    def endTime(self):
        '''The time up to which statistics are retrieved. Corresponds to server time. When
        endTime is omitted, the returned result includes up to the most recent
        metric value. When an endTime is specified, the returned samples include
        the sample at endTime.
        '''
        return self.data['endTime']

    @property
    def entity(self):
        '''The managed object whose performance statistics are being queried.
        '''
        return self.data['entity']

    @property
    def format(self):
        '''The format to be used while returning the statistics.
        '''
        return self.data['format']

    @property
    def intervalId(self):
        '''The interval (samplingPeriod), in seconds, for the performance statistics. For
        aggregated information, use one of the historical intervals for this
        property. See PerfInterval for more information. * To obtain the greatest
        detail, use the provider?s refreshRate for this property.
        '''
        return self.data['intervalId']

    @property
    def maxSample(self):
        '''Limits the number of samples returned. Defaults to the most recent sample (or
        samples), unless a time range is specified. Use this property only in
        conjunction with the intervalId to obtain real-time statistics (set the
        intervalId to the refreshRate. This property is ignored for historical
        statistics, and is not valid for the QueryPerfComposite operation.
        '''
        return self.data['maxSample']

    @property
    def metricId(self):
        '''The performance metrics to be retrieved. This property is required for the
        QueryPerfComposite operation.
        '''
        return self.data['metricId']

    @property
    def startTime(self):
        '''The server time from which to obtain counters. If not specified, defaults to the
        first available counter. When a startTime is specified, the returned
        samples do not include the sample at startTime.
        '''
        return self.data['startTime']

