
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class TaskInfo(DynamicData):
    '''This data object type contains all information about a task. A task represents an
        operation performed by VirtualCenter or ESX.
    '''
    
    def __init__(self, cancelable, cancelled, changeTag, completeTime, description, descriptionId, entity, entityName, error, eventChainId, key, locked, name, parentTaskKey, progress, queueTime, reason, result, rootTaskKey, startTime, state, task):
        # MUST define these
        super(TaskInfo, self).__init__()
    
        self.data['cancelable'] = cancelable
        self.data['cancelled'] = cancelled
        self.data['changeTag'] = changeTag
        self.data['completeTime'] = completeTime
        self.data['description'] = description
        self.data['descriptionId'] = descriptionId
        self.data['entity'] = entity
        self.data['entityName'] = entityName
        self.data['error'] = error
        self.data['eventChainId'] = eventChainId
        self.data['key'] = key
        self.data['locked'] = locked
        self.data['name'] = name
        self.data['parentTaskKey'] = parentTaskKey
        self.data['progress'] = progress
        self.data['queueTime'] = queueTime
        self.data['reason'] = reason
        self.data['result'] = result
        self.data['rootTaskKey'] = rootTaskKey
        self.data['startTime'] = startTime
        self.data['state'] = state
        self.data['task'] = task
    
    
    @property
    def cancelable(self):
        '''Flag to indicate whether or not the cancel task operation is supported.
        '''
        return self.data['cancelable']

    @property
    def cancelled(self):
        '''Flag to indicate whether or not the client requested cancellation of the task.
        '''
        return self.data['cancelled']

    @property
    def changeTag(self):
        '''The user entered tag to identify the operations and their side effects
        '''
        return self.data['changeTag']

    @property
    def completeTime(self):
        '''Time stamp when the task was completed (whether success or failure).
        '''
        return self.data['completeTime']

    @property
    def description(self):
        '''The description field of the task describes the current phase of operation of the
        task. For a task that does a single monolithic activity, this will be
        fixed and unchanging. For tasks that have various substeps, this field
        will change as the task progresses from one phase to another.
        '''
        return self.data['description']

    @property
    def descriptionId(self):
        '''An identifier for this operation. This includes publicly visible internal tasks
        and is a lookup in the TaskDescription methodInfo data object.
        '''
        return self.data['descriptionId']

    @property
    def entity(self):
        '''Managed entity to which the operation applies.
        '''
        return self.data['entity']

    @property
    def entityName(self):
        '''The name of the managed entity, locale-specific, retained for the history
        collector database.
        '''
        return self.data['entityName']

    @property
    def error(self):
        '''If the task state is "error", then this property contains the fault code.
        '''
        return self.data['error']

    @property
    def eventChainId(self):
        '''Event chain ID that leads to the corresponding events.
        '''
        return self.data['eventChainId']

    @property
    def key(self):
        '''The unique key for the task.
        '''
        return self.data['key']

    @property
    def locked(self):
        '''If the state of the task is "running", then this property is a list of managed
        entities that the operation has locked, with a shared lock.
        '''
        return self.data['locked']

    @property
    def name(self):
        '''The name of the operation that created the task. This is not set for internal
        tasks.
        '''
        return self.data['name']

    @property
    def parentTaskKey(self):
        '''Tasks can be cretaed by another task. This shows key of the task spun off this
        task. This is to track causality between tasks.
        '''
        return self.data['parentTaskKey']

    @property
    def progress(self):
        '''If the task state is "running", then this property contains a progress
        measurement, expressed as percentage completed, from 0 to 100.
        '''
        return self.data['progress']

    @property
    def queueTime(self):
        '''Time stamp when the task was created.
        '''
        return self.data['queueTime']

    @property
    def reason(self):
        '''Kind of entity responsible for creating this task.
        '''
        return self.data['reason']

    @property
    def result(self):
        '''If the task state is "success", then this property may be used to hold a return
        value.
        '''
        return self.data['result']

    @property
    def rootTaskKey(self):
        '''Tasks can be cretaed by another task and such creation can go on for multiple
        levels. This is the key of the task that started the chain of tasks.
        '''
        return self.data['rootTaskKey']

    @property
    def startTime(self):
        '''Time stamp when the task started running.
        '''
        return self.data['startTime']

    @property
    def state(self):
        '''Runtime status of the task.
        '''
        return self.data['state']

    @property
    def task(self):
        '''The managed object that represents this task.
        '''
        return self.data['task']

