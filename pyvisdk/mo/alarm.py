
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class Alarm(ExtensibleManagedObject):
    '''This managed object type defines an alarm that is triggered and an action that
    occurs due to the triggered alarm when certain conditions are met on a specific
    ManagedEntity object.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.Alarm):
        super(Alarm, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def info(self):
        '''Information about this alarm.'''
        return self.update('info')
    
    
    
    def ReconfigureAlarm(self):
        '''Reconfigures the alarm properties. This operation requires access privileges on
        the entity with which the alarm is associated.In addition to the Alarm.Edit
        privilege, may also require the Global.ScriptAction if a RunScriptAction action
        is specified in the AlarmSpec.
        :rtype: None
        :returns: 
        '''
        return self.delegate("ReconfigureAlarm")()
    
    def RemoveAlarm(self):
        '''Removes the alarm.
        :rtype: None
        :returns: 
        '''
        return self.delegate("RemoveAlarm")()