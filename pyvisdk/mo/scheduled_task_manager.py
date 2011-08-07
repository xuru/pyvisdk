
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ScheduledTaskManager(BaseEntity):
    '''Object manager for scheduled tasks.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.ScheduledTaskManager):
        # MUST define these
        super(ScheduledTaskManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def description(self):
        '''Static descriptive strings used in scheduled tasks.
        '''
        return self.update('description')

    @property
    def scheduledTask(self):
        '''All available scheduled tasks.
        '''
        return self.update('scheduledTask')


    def CreateObjectScheduledTask(self, obj):
        '''Creates a scheduled task.

        :param obj: The object. If not specified, all scheduled tasks are returned for visible
        entities and visible ManagedObjects.


        :rtype: ManagedObjectReference[] to a ScheduledTask[] 

        '''
        
        return self.delegate("CreateObjectScheduledTask")(obj)
        

    def CreateScheduledTask(self, obj):
        '''Creates a scheduled task.

        :param obj: The object. If not specified, all scheduled tasks are returned for visible
        entities and visible ManagedObjects.


        :rtype: ManagedObjectReference[] to a ScheduledTask[] 

        '''
        
        return self.delegate("CreateScheduledTask")(obj)
        

    def RetrieveEntityScheduledTask(self, obj):
        '''Available scheduled tasks defined on the entity.

        :param obj: The object. If not specified, all scheduled tasks are returned for visible
        entities and visible ManagedObjects.


        :rtype: ManagedObjectReference[] to a ScheduledTask[] 

        '''
        
        return self.delegate("RetrieveEntityScheduledTask")(obj)
        

    def RetrieveObjectScheduledTask(self, obj):
        '''Available scheduled tasks defined on the object.

        :param obj: The object. If not specified, all scheduled tasks are returned for visible
        entities and visible ManagedObjects.


        :rtype: ManagedObjectReference[] to a ScheduledTask[] 

        '''
        
        return self.delegate("RetrieveObjectScheduledTask")(obj)
        
