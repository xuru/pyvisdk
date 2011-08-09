
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class TaskFilterSpec(DynamicData):
    '''This data object type defines the specification for the task filter used to query
        tasks in the history collector database. The client creates a task history
        collector with a filter specification, then retrieves the tasks from the
        task history collector.
    '''
    
    def __init__(self, alarm, entity, eventChainId, parentTaskKey, rootTaskKey, scheduledTask, state, tag, time, userName):
        # MUST define these
        super(TaskFilterSpec, self).__init__()
    
        self.data['alarm'] = alarm
        self.data['entity'] = entity
        self.data['eventChainId'] = eventChainId
        self.data['parentTaskKey'] = parentTaskKey
        self.data['rootTaskKey'] = rootTaskKey
        self.data['scheduledTask'] = scheduledTask
        self.data['state'] = state
        self.data['tag'] = tag
        self.data['time'] = time
        self.data['userName'] = userName
    
    
    @property
    def alarm(self):
        '''This property, if provided, limits the set of collected tasks to those associated
        with the specified alarm. If not provided, tasks are collected regardless
        of their association with alarms.
        '''
        return self.data['alarm']

    @property
    def entity(self):
        '''The filter specification for retrieving tasks by managed entity. If not provided,
        then the tasks attached to all managed entities are collected.
        '''
        return self.data['entity']

    @property
    def eventChainId(self):
        '''The filter specification for retrieving tasks by chain ID. If it is set, tasks not
        with the given eventChainId will be filtered out. If the property is not
        set, tasks' chain ID is disregarded for filtering purposes.
        '''
        return self.data['eventChainId']

    @property
    def parentTaskKey(self):
        '''The filter specification for retrieving tasks by parentTaskKey. If it is set,
        tasks not with the given parentTaskKey(s) will be filtered out. If the
        property is not set, tasks' parentTaskKey is disregarded for filtering
        purposes.
        '''
        return self.data['parentTaskKey']

    @property
    def rootTaskKey(self):
        '''The filter specification for retrieving tasks by rootTaskKey. If it is set, tasks
        not with the given rootTaskKey(s) will be filtered out. If the property is
        not set, tasks' rootTaskKey is disregarded for filtering purposes.
        '''
        return self.data['rootTaskKey']

    @property
    def scheduledTask(self):
        '''This property, if provided, limits the set of collected tasks to those associated
        with the specified scheduled task. If not provided, tasks are collected
        regardless of their association with any scheduled task.
        '''
        return self.data['scheduledTask']

    @property
    def state(self):
        '''This property, if provided, limits the set of collected tasks by their states.
        Task states are enumerated in State. If not provided, tasks are collected
        regardless of their state.
        '''
        return self.data['state']

    @property
    def tag(self):
        '''The filter specification for retrieving tasks by tag. If it is set, tasks not with
        the given tag(s) will be filtered out. If the property is not set, tasks'
        tag is disregarded for filtering purposes. If it is set, and includes an
        empty string, tasks without a tag will be returned.
        '''
        return self.data['tag']

    @property
    def time(self):
        '''The filter specification for retrieving tasks by time. If not provided, then the
        tasks with any time stamp are collected.
        '''
        return self.data['time']

    @property
    def userName(self):
        '''The filter specification for retrieving tasks by user name. If not provided, then
        the tasks belonging to any user are collected.
        '''
        return self.data['userName']

