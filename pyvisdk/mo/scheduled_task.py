
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ScheduledTask(ExtensibleManagedObject):
    '''The scheduled task object.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.ScheduledTask):
        super(ScheduledTask, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def info(self):
        '''Information about the current scheduled task.'''
        return self.update('info')
    
    
    
    def ReconfigureScheduledTask(self):
        '''Reconfigures the scheduled task properties.
        :rtype: None
        :returns: 
        '''
        return self.delegate("ReconfigureScheduledTask")()
    
    def RemoveScheduledTask(self):
        '''Removes the scheduled task.
        :rtype: None
        :returns: 
        '''
        return self.delegate("RemoveScheduledTask")()
    
    def RunScheduledTask(self):
        '''Runs the scheduled task immediately. The schedule for future runs remains in
        effect.
        :rtype: None
        :returns: 
        '''
        return self.delegate("RunScheduledTask")()