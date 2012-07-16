
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class TaskManager(BaseEntity):
    '''The TaskManager managed object provides an interface for creating and managing
    Task managed objects. Many operations are non-blocking, returning a Task
    managed object that can be monitored by a client application. Task managed
    objects may also be accessed through the TaskManager.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.TaskManager):
        super(TaskManager, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def description(self):
        '''Locale-specific, static strings that describe Task information to users.'''
        return self.update('description')
    @property
    def maxCollector(self):
        '''Maximum number of TaskHistoryCollector data objects that can exist
        concurrently, per client.'''
        return self.update('maxCollector')
    @property
    def recentTask(self):
        '''A list of Task managed objects that completed recently, that are currently
        running, or that are queued to run.'''
        return self.update('recentTask')

    
    
    def CreateCollectorForTasks(self, filter):
        '''Creates a TaskHistoryCollector, a specialized HistoryCollector that gathers
        TaskInfo data objects.Creates a TaskHistoryCollector, a specialized
        HistoryCollector that gathers TaskInfo data objects.
        
        :param filter: The specification for the task query filter.
        
        '''
        return self.delegate("CreateCollectorForTasks")(filter)
    
    def CreateTask(self, obj, taskTypeId, cancelable, initiatedBy=None, parentTaskKey=None):
        '''Creates a new Task, specifying the object with which the Task is associated,
        the type of task, and whether the task is cancelable. Use this operation in
        conjunction with the ExtensionManager.
        
        :param obj: ManagedObject with which Task will be associated
        
        :param taskTypeId: Extension registered task type identifier for type of task being created
        
        :param initiatedBy: The name of the user on whose behalf the Extension is creating the task
        
        :param cancelable: True if the task should be cancelable, else false
        
        :param parentTaskKey: Key of the task that is the parent of this taskvSphere API 4.0
        
        '''
        return self.delegate("CreateTask")(obj, taskTypeId, initiatedBy, cancelable, parentTaskKey)