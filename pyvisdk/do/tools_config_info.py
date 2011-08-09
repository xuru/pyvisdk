
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ToolsConfigInfo(DynamicData):
    '''ToolsConfigInfo is a data object type containing settings for the VMware Tools
        software running in the guest operating system.
    '''
    
    def __init__(self, afterPowerOn, afterResume, beforeGuestReboot, beforeGuestShutdown, beforeGuestStandby, pendingCustomization, syncTimeWithHost, toolsUpgradePolicy, toolsVersion):
        # MUST define these
        super(ToolsConfigInfo, self).__init__()
    
        self.data['afterPowerOn'] = afterPowerOn
        self.data['afterResume'] = afterResume
        self.data['beforeGuestReboot'] = beforeGuestReboot
        self.data['beforeGuestShutdown'] = beforeGuestShutdown
        self.data['beforeGuestStandby'] = beforeGuestStandby
        self.data['pendingCustomization'] = pendingCustomization
        self.data['syncTimeWithHost'] = syncTimeWithHost
        self.data['toolsUpgradePolicy'] = toolsUpgradePolicy
        self.data['toolsVersion'] = toolsVersion
    
    
    @property
    def afterPowerOn(self):
        '''Flag to specify whether or not scripts should run after the virtual machine powers
        on.
        '''
        return self.data['afterPowerOn']

    @property
    def afterResume(self):
        '''Flag to specify whether or not scripts should run after the virtual machine
        resumes.
        '''
        return self.data['afterResume']

    @property
    def beforeGuestReboot(self):
        '''Flag to specify whether or not scripts should run before the virtual machine
        reboots.
        '''
        return self.data['beforeGuestReboot']

    @property
    def beforeGuestShutdown(self):
        '''Flag to specify whether or not scripts should run before the virtual machine
        powers off.
        '''
        return self.data['beforeGuestShutdown']

    @property
    def beforeGuestStandby(self):
        '''Flag to specify whether or not scripts should run before the virtual machine
        suspends.
        '''
        return self.data['beforeGuestStandby']

    @property
    def pendingCustomization(self):
        '''When set, this indicates that a customization operation is pending on the VM. The
        value represents the filename of the customization package on the host.
        '''
        return self.data['pendingCustomization']

    @property
    def syncTimeWithHost(self):
        '''Indicates whether or not the tools program will sync time with the host time.
        '''
        return self.data['syncTimeWithHost']

    @property
    def toolsUpgradePolicy(self):
        '''Tools upgrade policy setting for the virtual machine.
        '''
        return self.data['toolsUpgradePolicy']

    @property
    def toolsVersion(self):
        '''Version of VMware Tools installed on the guest operating system.
        '''
        return self.data['toolsVersion']

