
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ScheduledTaskManager(BaseEntity):
    '''Object manager for scheduled tasks.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.ScheduledTaskManager):
        super(ScheduledTaskManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def description(self):
        '''Static descriptive strings used in scheduled tasks.'''
        return self.update('description')
    @property
    def scheduledTask(self):
        '''All available scheduled tasks.'''
        return self.update('scheduledTask')
    
    
    
    def CreateObjectScheduledTask(self):
        '''Creates a scheduled task.
        :rtype: ManagedObjectReference to a ScheduledTask
        :returns: 
        '''
        return self.delegate("CreateObjectScheduledTask")()
    
    def CreateScheduledTask(self):
        '''Creates a scheduled task.
        :rtype: ManagedObjectReference to a ScheduledTask
        :returns: 
        '''
        return self.delegate("CreateScheduledTask")()
    
    def RetrieveEntityScheduledTask(self):
        '''Available scheduled tasks defined on the entity.
        :rtype: ManagedObjectReference[] to a ScheduledTask[]
        :returns: 
        '''
        return self.delegate("RetrieveEntityScheduledTask")()
    
    def RetrieveObjectScheduledTask(self):
        '''Available scheduled tasks defined on the object.
        :rtype: ManagedObjectReference[] to a ScheduledTask[]
        :returns: 
        '''
        return self.delegate("RetrieveObjectScheduledTask")()