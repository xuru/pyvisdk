
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


    def CreateObjectScheduledTask(self, obj, spec):
        '''Creates a scheduled task.

        :param obj: The managed object for which the scheduled task triggers an action. You can
        schedule tasks on any managed object.

        :param spec: The specification for the new scheduled task.


        :rtype: ManagedObjectReference to a ScheduledTask 

        '''
        
        return self.delegate("CreateObjectScheduledTask")(obj,spec)
        

    def CreateScheduledTask(self, entity, spec):
        '''Creates a scheduled task.

        :param entity: to a ManagedEntityThe managed entity (or entities) for which the scheduled task
        triggers an action. You can schedule tasks on any managed entity. If the
        scheduled task is associated with a leaf node in the inventory tree, it
        applies only to a single entity (virtual machine or host). If the task is
        associated with a folder, a datacenter, a compute resource, or a resource
        pool, it applies to the virtual machine or host descendants of the entity.

        :param spec: The specification for the new scheduled task.


        :rtype: ManagedObjectReference to a ScheduledTask 

        '''
        
        return self.delegate("CreateScheduledTask")(entity,spec)
        

    def RetrieveEntityScheduledTask(self, entity):
        '''Available scheduled tasks defined on the entity.

        :param entity: to a ManagedEntityThe entity. If null, all scheduled tasks are returned for
        visible entities.


        :rtype: ManagedObjectReference[] to a ScheduledTask[] 

        '''
        
        return self.delegate("RetrieveEntityScheduledTask")(entity)
        

    def RetrieveObjectScheduledTask(self, obj):
        '''Available scheduled tasks defined on the object.

        :param obj: The object. If not specified, all scheduled tasks are returned for visible
        entities and visible ManagedObjects.


        :rtype: ManagedObjectReference[] to a ScheduledTask[] 

        '''
        
        return self.delegate("RetrieveObjectScheduledTask")(obj)
        