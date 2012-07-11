
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

    
    
    def ReconfigureAlarm(self, spec):
        '''Reconfigures the alarm properties. This operation requires access privileges on
        the entity with which the alarm is associated.Reconfigures the alarm
        properties. This operation requires access privileges on the entity with which
        the alarm is associated.
        
        :param spec: The new specification for the alarm.
        
        '''
        return self.delegate("ReconfigureAlarm")(spec)
    
    def RemoveAlarm(self):
        '''Removes the alarm.
        
        '''
        return self.delegate("RemoveAlarm")()