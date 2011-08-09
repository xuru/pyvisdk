
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVSPolicy(DynamicData):
    '''The switch usage policy types
    '''
    
    def __init__(self, autoPreInstallAllowed, autoUpgradeAllowed, partialUpgradeAllowed):
        # MUST define these
        super(DVSPolicy, self).__init__()
    
        self.data['autoPreInstallAllowed'] = autoPreInstallAllowed
        self.data['autoUpgradeAllowed'] = autoUpgradeAllowed
        self.data['partialUpgradeAllowed'] = partialUpgradeAllowed
    
    
    @property
    def autoPreInstallAllowed(self):
        '''Whether downloading a new proxy VirtualSwitch module to the host is allowed to be
        automatically executed by the switch.
        '''
        return self.data['autoPreInstallAllowed']

    @property
    def autoUpgradeAllowed(self):
        '''Whether upgrading of the switch is allowed to be automatically executed by the
        switch.
        '''
        return self.data['autoUpgradeAllowed']

    @property
    def partialUpgradeAllowed(self):
        '''Whether to allow upgrading a switch when some of the hosts failed to install the
        needed module. The vCenter Server will reattempt the pre-install operation
        of the host module on those failed hosts, whenever they reconnect to
        vCenter.
        '''
        return self.data['partialUpgradeAllowed']

