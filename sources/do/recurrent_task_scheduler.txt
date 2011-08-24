
================================================================================
RecurrentTaskScheduler
================================================================================


.. describe:: Extended by
    
    :py:class:`~pyvisdk.do.hourly_task_scheduler.HourlyTaskScheduler`
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.task_scheduler.TaskScheduler`
    
.. class:: pyvisdk.do.recurrent_task_scheduler.RecurrentTaskScheduler
    
    .. py:attribute:: interval
    
        How often to run the scheduled task. The value must be greater than or equal to 1. The default value is 1. The interval acts as a multiplier for the unit of time associated with a particular scheduler (hours, days, weeks, or months). For example, setting the HourlyTaskScheduler interval to 4 causes the task to run every 4 hours.
        
    