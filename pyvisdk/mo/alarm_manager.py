
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

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

    
    
    def AcknowledgeAlarm(self, alarm, entity):
        '''Acknowledge the alarm on a managed entity. The actions associated with the
        alarm will not fire until the alarm's next distinct occurrence; that is, until
        after the alarm has entered the green or gray states at least once. Calling
        this method on an acknowledged or non-triggered alarm.
        
        :param alarm: The Alarm to acknowledge.
        
        :param entity: The ManagedEntity for which to acknowledge the Alarm.
        
        '''
        return self.delegate("AcknowledgeAlarm")(alarm, entity)
    
    def AreAlarmActionsEnabled(self, entity):
        '''Returns true if alarm actions are enabled on the specified managed entity.
        
        :param entity: The managed entity to look up.
        
        '''
        return self.delegate("AreAlarmActionsEnabled")(entity)
    
    def CreateAlarm(self, entity, spec):
        '''Creates an alarm.Creates an alarm.
        
        :param entity: The entity with which the alarm is associated.
        
        :param spec: The specification for the new alarm.
        
        '''
        return self.delegate("CreateAlarm")(entity, spec)
    
    def EnableAlarmActions(self, entity, enabled):
        '''Enables or disables alarms on the specified managed entity.
        
        :param entity: The managed entity on which to set a schedule.
        
        :param enabled: true, if alarms are enabled during the schedule.
        
        '''
        return self.delegate("EnableAlarmActions")(entity, enabled)
    
    def GetAlarm(self, entity=None):
        '''Available alarms defined on the entity. These alarms do not include any
        inherited alarms; that is, alarms associated with parent entities.
        
        :param entity: The entity. If not set, alarms are returned for all visible entities.
        
        '''
        return self.delegate("GetAlarm")(entity)
    
    def GetAlarmState(self, entity):
        '''The state of instantiated alarms on the entity.
        
        :param entity: The entity.
        
        '''
        return self.delegate("GetAlarmState")(entity)