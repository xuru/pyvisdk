
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
    
    

    def CreateScheduledTask(self, spec):
        '''Creates a scheduled task.

        :param spec: The specification for the new scheduled task.


        :rtype: ManagedObjectReference to a ScheduledTask 

        '''
        
        return self.delegate("CreateScheduledTask")(spec)
        

    def RetrieveEntityScheduledTask(self):
        '''Available scheduled tasks defined on the entity.

        :rtype: ManagedObjectReference[] to a ScheduledTask[] 

        '''
        
        return self.delegate("RetrieveEntityScheduledTask")()
        

    def CreateObjectScheduledTask(self, spec):
        '''Creates a scheduled task.

        :param spec: The specification for the new scheduled task.


        :rtype: ManagedObjectReference to a ScheduledTask 

        '''
        
        return self.delegate("CreateObjectScheduledTask")(spec)
        

    def RetrieveObjectScheduledTask(self):
        '''Available scheduled tasks defined on the object.

        :rtype: ManagedObjectReference[] to a ScheduledTask[] 

        '''
        
        return self.delegate("RetrieveObjectScheduledTask")()
        
