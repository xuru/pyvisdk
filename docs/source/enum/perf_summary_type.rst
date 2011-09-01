
==================================================================================================
PerfSummaryType
==================================================================================================

.. describe:: PerfSummaryType

    Indicates how multiple samples of a specific counter type are transformed into a single statistical value.
    
    
    .. py:data:: PerfSummaryType.average
    
        The actual value collected or the average of all values collected during the summary period.
        
    
    .. py:data:: PerfSummaryType.latest
    
        The most recent value of the performance counter over the summarization period.
        
    
    .. py:data:: PerfSummaryType.maximum
    
        The maximum value of the performance counter value over the summarization period.
        
    
    .. py:data:: PerfSummaryType.minimum
    
        The minimum value of the performance counter value over the summarization period.
        
    
    .. py:data:: PerfSummaryType.none
    
        The counter is never rolled up.
        
    
    .. py:data:: PerfSummaryType.summation
    
        The sum of all the values of the performance counter over the summarization period.
        
    