
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AutoStartDefaults(DynamicData):
    '''Defines the system default auto-start/auto-stop values.
    '''
    
    def __init__(self, enabled, startDelay, stopAction, stopDelay, waitForHeartbeat):
        # MUST define these
        super(AutoStartDefaults, self).__init__()
    
        self.data['enabled'] = enabled
        self.data['startDelay'] = startDelay
        self.data['stopAction'] = stopAction
        self.data['stopDelay'] = stopDelay
        self.data['waitForHeartbeat'] = waitForHeartbeat
    
    
    @property
    def enabled(self):
        '''Indicates whether or not auto-start manager is enabled.
        '''
        return self.data['enabled']

    @property
    def startDelay(self):
        '''System-default autoStart delay in seconds. The default is 120 seconds.
        '''
        return self.data['startDelay']

    @property
    def stopAction(self):
        '''System-default power-off action. Used if the stopAction string in the
        AutoPowerInfo object for a particular machine is set to systemDefault. If
        stopAction and startAction for a virtual machine are both set to none,
        that virtual machine is removed from the AutoStart sequence.
        '''
        return self.data['stopAction']

    @property
    def stopDelay(self):
        '''System-default autoStop delay in seconds. The default is 120 seconds.
        '''
        return self.data['stopDelay']

    @property
    def waitForHeartbeat(self):
        '''System-default waitForHeartbeat setting.
        '''
        return self.data['waitForHeartbeat']

