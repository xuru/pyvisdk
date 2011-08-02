
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AlarmManager(BaseEntity):
    '''The alarm manager is a singleton object for managing alarms within a service
        instance.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.AlarmManager):
        # MUST define these
        super(AlarmManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def defaultExpression(self):
        '''
        The default setting for each alarm expression, used to populate the initial client
        wizard screen.
        '''
        return self.update('defaultExpression')

    @property
    def description(self):
        '''
        The static descriptive strings used in alarms.
        '''
        return self.update('description')


    def AcknowledgeAlarm(self):
        '''Acknowledge the alarm on a managed entity. The actions associated with the alarm
        will not fire until the alarm's next distinct occurrence; that is, until
        after the alarm has entered the green or gray states at least once.
        Calling this method on an acknowledged or non-triggered alarm.
        '''
        
        return self.delegate("AcknowledgeAlarm")()
        

    def EnableAlarmActions(self, enabled):
        '''Enables or disables alarms on the specified managed entity.

        :param enabled: true, if alarms are enabled during the schedule.

        '''
        
        return self.delegate("EnableAlarmActions")(enabled)
        

    def AreAlarmActionsEnabled(self):
        '''Returns true if alarm actions are enabled on the specified managed entity.

        :rtype: xsd:boolean 

        '''
        
        return self.delegate("AreAlarmActionsEnabled")()
        

    def GetAlarm(self):
        '''Available alarms defined on the entity. These alarms do not include any inherited
        alarms; that is, alarms associated with parent entities.

        :rtype: ManagedObjectReference[] to a Alarm[] 

        '''
        
        return self.delegate("GetAlarm")()
        

    def CreateAlarm(self, spec):
        '''Creates an alarm.In addition to the Alarm.Create privilege, may also require the
        Global.ScriptAction if a RunScriptAction action is specified in the
        AlarmSpec.

        :param spec: The specification for the new alarm.


        :rtype: ManagedObjectReference to a Alarm 

        '''
        
        return self.delegate("CreateAlarm")(spec)
        

    def GetAlarmState(self):
        '''The state of instantiated alarms on the entity.

        :rtype: AlarmState[] 

        '''
        
        return self.delegate("GetAlarmState")()
        
