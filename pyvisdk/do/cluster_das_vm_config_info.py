
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterDasVmConfigInfo(DynamicData):
    '''The ClusterDasVmConfigInfo data object contains the HA configuration for a single
        virtual machine.All fields are optional. If you set the parameter to when
        you call ReconfigureComputeResource_Task, an unset property has no effect
        on the existing property value in the cluster configuration on the Server.
        If you set the parameter to when you reconfigure a cluster, the cluster
        configuration is reverted to the default values, then the new
        configuration values are applied.
    '''
    
    def __init__(self, dasSettings, key, powerOffOnIsolation, restartPriority):
        # MUST define these
        super(ClusterDasVmConfigInfo, self).__init__()
    
        self.data['dasSettings'] = dasSettings
        self.data['key'] = key
        self.data['powerOffOnIsolation'] = powerOffOnIsolation
        self.data['restartPriority'] = restartPriority
    
    
    @property
    def dasSettings(self):
        '''HA settings that apply to this virtual machine.
        '''
        return self.data['dasSettings']

    @property
    def key(self):
        '''Reference to the virtual machine.
        '''
        return self.data['key']

    @property
    def powerOffOnIsolation(self):
        '''Flag to indicate whether or not the virtual machine should be powered off if a
        host determines that it is isolated from the rest of the compute resource.
        '''
        return self.data['powerOffOnIsolation']

    @property
    def restartPriority(self):
        '''Restart priority for a virtual machine.
        '''
        return self.data['restartPriority']

