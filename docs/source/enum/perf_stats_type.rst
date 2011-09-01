
==================================================================================================
PerfStatsType
==================================================================================================

.. describe:: PerfStatsType

    Indicates the type of statistical measurement that a counters value represents. Valid types are absolute, delta, or rate.
    
    
    .. py:data:: PerfStatsType.absolute
    
        Represents an actual value, level, or state of the counter. For example, the uptime counter ( group) represents the actual number of seconds since startup. The capacity counter represents the actual configured size of the specified datastore. In other words, number of samples, samplingPeriod, and intervals have no bearing on an absolute counters value.
        
    
    .. py:data:: PerfStatsType.delta
    
        Represents an amount of change for the counter during the samplingPeriod as compared to the previous interval. The first sampling interval
        
    
    .. py:data:: PerfStatsType.rate
    
        Represents a value that has been normalized over the samplingPeriod, enabling values for the same counter type to be compared, regardless of interval. For example, the number of reads per second.
        
    