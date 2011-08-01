
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class TaskManager(BaseEntity):
    '''The TaskManager managed object provides an interface for creating and managing
        Task managed objects. Many operations are non-blocking, returning a Task
        managed object that can be monitored by a client application. Task managed
        objects may also be accessed through the TaskManager.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.TaskManager):
        # MUST define these
        super(TaskManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def maxCollector(self):
        '''
        Maximum number of TaskHistoryCollector data objects that can exist concurrently,
        per client.
        '''
        return self.update('maxCollector')


    def CreateTask(self, cancelable, taskTypeId, obj):
        '''Creates a new Task, specifying the object with which the Task is associated, the
        type of task, and whether the task is cancelable. Use this operation in
        conjunction with the ExtensionManager.

        :param cancelable: True if the task should be cancelable, else false

        :param taskTypeId: Extension registered task type identifier for type of task being created

        :param obj: ManagedObject with which Task will be associated


        :rtype: TaskInfo 

        '''
        
        return self.delegate("CreateTask")(cancelable,taskTypeId,obj)
        

    def CreateCollectorForTasks(self, filter):
        '''Creates a TaskHistoryCollector, a specialized HistoryCollector that gathers
        TaskInfo data objects.A TaskHistoryCollector does not persist beyond the
        current client session.

        :param filter: The specification for the task query filter.


        :rtype: ManagedObjectReference to a TaskHistoryCollector 

        '''
        
        return self.delegate("CreateCollectorForTasks")(filter)
        
