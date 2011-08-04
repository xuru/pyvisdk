
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class Alarm(ExtensibleManagedObject):
    '''
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.Alarm):
        # MUST define these
        super(Alarm, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def info(self):
        '''Information about this alarm.
        '''
        return self.update('info')


    def ReconfigureAlarm(self, spec):
        '''Reconfigures the alarm properties. This operation requires access privileges on
        the entity with which the alarm is associated.In addition to the
        Alarm.Edit privilege, may also require the Global.ScriptAction if a
        RunScriptAction action is specified in the AlarmSpec.

        :param spec: The new specification for the alarm.

        '''
        
        return self.delegate("ReconfigureAlarm")(spec)
        

    def RemoveAlarm(self):
        '''Removes the alarm.
        '''
        
        return self.delegate("RemoveAlarm")()
        
