
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AlarmManager(BaseEntity):
    '''The alarm manager is a singleton object for managing alarms within a service
    instance.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.AlarmManager):
        super(AlarmManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def defaultExpression(self):
        '''The default setting for each alarm expression, used to populate the initial
    client wizard screen.'''
        return self.update('defaultExpression')
    @property
    def description(self):
        '''The static descriptive strings used in alarms.'''
        return self.update('description')
    
    
    
    def AcknowledgeAlarm(self):
        '''Acknowledge the alarm on a managed entity. The actions associated with the
        alarm will not fire until the alarm's next distinct occurrence; that is, until
        after the alarm has entered the green or gray states at least once. Calling
        this method on an acknowledged or non-triggered alarm.
        :rtype: None
        :returns: 
        '''
        return self.delegate("AcknowledgeAlarm")()
    
    def AreAlarmActionsEnabled(self):
        '''Returns true if alarm actions are enabled on the specified managed entity.
        :rtype: 
        :returns: 
        '''
        return self.delegate("AreAlarmActionsEnabled")()
    
    def CreateAlarm(self):
        '''Creates an alarm.In addition to the Alarm.Create privilege, may also require
        the Global.ScriptAction if a RunScriptAction action is specified in the
        AlarmSpec.
        :rtype: ManagedObjectReference to a Alarm
        :returns: 
        '''
        return self.delegate("CreateAlarm")()
    
    def EnableAlarmActions(self):
        '''Enables or disables alarms on the specified managed entity.
        :rtype: None
        :returns: 
        '''
        return self.delegate("EnableAlarmActions")()
    
    def GetAlarm(self):
        '''Available alarms defined on the entity. These alarms do not include any
        inherited alarms; that is, alarms associated with parent entities.
        :rtype: ManagedObjectReference[] to a Alarm[]
        :returns: 
        '''
        return self.delegate("GetAlarm")()
    
    def GetAlarmState(self):
        '''The state of instantiated alarms on the entity.
        :rtype: 
        :returns: 
        '''
        return self.delegate("GetAlarmState")()