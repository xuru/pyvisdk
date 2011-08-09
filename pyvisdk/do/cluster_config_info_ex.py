
from pyvisdk.do.compute_resource_config_info import ComputeResourceConfigInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterConfigInfoEx(ComputeResourceConfigInfo):
    '''The ClusterConfigInfoEx data object describes a complete cluster configuration.
        For information about configuring a cluster, see ClusterConfigSpecEx.
    '''
    
    def __init__(self, dasConfig, dasVmConfig, dpmConfigInfo, dpmHostConfig, drsConfig, drsVmConfig, group, rule):
        # MUST define these
        super(ClusterConfigInfoEx, self).__init__()
    
        self.data['dasConfig'] = dasConfig
        self.data['dasVmConfig'] = dasVmConfig
        self.data['dpmConfigInfo'] = dpmConfigInfo
        self.data['dpmHostConfig'] = dpmHostConfig
        self.data['drsConfig'] = drsConfig
        self.data['drsVmConfig'] = drsVmConfig
        self.data['group'] = group
        self.data['rule'] = rule
    
    
    @property
    def dasConfig(self):
        '''Cluster-wide configuration of the VMware HA service.
        '''
        return self.data['dasConfig']

    @property
    def dasVmConfig(self):
        '''List of virtual machine configurations for the VMware HA service. Each entry
        applies to one virtual machine.
        '''
        return self.data['dasVmConfig']

    @property
    def dpmConfigInfo(self):
        '''Cluster-wide configuration of the VMware DPM service.
        '''
        return self.data['dpmConfigInfo']

    @property
    def dpmHostConfig(self):
        '''List of host configurations for the VMware DPM service. Each entry applies to one
        virtual machine.
        '''
        return self.data['dpmHostConfig']

    @property
    def drsConfig(self):
        '''Cluster-wide configuration of the VMware DRS service.
        '''
        return self.data['drsConfig']

    @property
    def drsVmConfig(self):
        '''List of virtual machine configurations for the VMware DRS service. Each entry
        applies to one virtual machine.
        '''
        return self.data['drsVmConfig']

    @property
    def group(self):
        '''Cluster-wide groups.
        '''
        return self.data['group']

    @property
    def rule(self):
        '''Cluster-wide rules.
        '''
        return self.data['rule']

