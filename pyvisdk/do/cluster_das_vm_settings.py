
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterDasVmSettings(DynamicData):
    '''The ClusterDasVmSettings data object contains the HA configuration settings
        specified for a single virtual machine (identified by
        ClusterDasVmConfigInfo.key) or as cluster-wide defaults
        (ClusterDasConfigInfo.defaultVmSettings).All fields are optional. If you
        set the parameter to when you call ReconfigureComputeResource_Task, an
        unset property has no effect on the existing property value in the cluster
        configuration on the Server. If you set the parameter to when you
        reconfigure a cluster, the cluster configuration is reverted to the
        default values, then the new configuration values are applied.
    '''
    
    def __init__(self, isolationResponse, restartPriority, vmToolsMonitoringSettings):
        # MUST define these
        super(ClusterDasVmSettings, self).__init__()
    
        self.data['isolationResponse'] = isolationResponse
        self.data['restartPriority'] = restartPriority
        self.data['vmToolsMonitoringSettings'] = vmToolsMonitoringSettings
    
    
    @property
    def isolationResponse(self):
        '''Indicates whether or not the virtual machine should be powered off if a host
        determines that it is isolated from the rest of the compute resource.
        '''
        return self.data['isolationResponse']

    @property
    def restartPriority(self):
        '''Restart priority for a virtual machine.
        '''
        return self.data['restartPriority']

    @property
    def vmToolsMonitoringSettings(self):
        '''Configuration for the VM Health Monitoring Service.
        '''
        return self.data['vmToolsMonitoringSettings']

