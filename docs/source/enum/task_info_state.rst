
==================================================================================================
TaskInfoState
==================================================================================================

.. describe:: TaskInfoState

    List of possible states of a task.
    
    
    .. py:data:: TaskInfoState.error
    
        When a running task has encountered an error.
        
    
    .. py:data:: TaskInfoState.queued
    
        When there are too many tasks for threads to handle.
        
    
    .. py:data:: TaskInfoState.running
    
        When the busy thread is freed from its current task by finishing the task, it picks a queued task to run. Then the queued tasks are marked as running.
        
    
    .. py:data:: TaskInfoState.success
    
        When a running task has completed.
        
    