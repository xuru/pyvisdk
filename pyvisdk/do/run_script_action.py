
from pyvisdk.do.action import Action
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class RunScriptAction(Action):
    '''This data object type specifies a script that is triggered by an alarm. You can
        use any elements of the ActionParameter enumerated list as part of your
        script to provide information available at runtime.
    '''
    
    def __init__(self, script):
        # MUST define these
        super(RunScriptAction, self).__init__()
    
        self.data['script'] = script
    
    
    @property
    def script(self):
        '''The fully-qualified path to a shell script that runs on the VirtualCenter server
        as a result of an alarm.
        '''
        return self.data['script']

