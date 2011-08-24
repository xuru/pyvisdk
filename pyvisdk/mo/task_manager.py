
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
    
    
    
    def CreateCollectorForTasks(self):
        '''Creates a TaskHistoryCollector, a specialized HistoryCollector that gathers
        TaskInfo data objects.A TaskHistoryCollector does not persist beyond the
        current client session.
        :rtype: ManagedObjectReference to a TaskHistoryCollector
        :returns: 
        '''
        return self.delegate("CreateCollectorForTasks")()
    
    def CreateTask(self):
        '''Creates a new Task, specifying the object with which the Task is associated,
        the type of task, and whether the task is cancelable. Use this operation in
        conjunction with the ExtensionManager.
        :rtype: 
        :returns: 
        '''
        return self.delegate("CreateTask")()