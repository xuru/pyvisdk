
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterConfigInfo(DynamicData):
    '''A complete cluster configuration.
    '''
    
    def __init__(self, dasConfig, dasVmConfig, drsConfig, drsVmConfig, rule):
        # MUST define these
        super(ClusterConfigInfo, self).__init__()
    
        self.data['dasConfig'] = dasConfig
        self.data['dasVmConfig'] = dasVmConfig
        self.data['drsConfig'] = drsConfig
        self.data['drsVmConfig'] = drsVmConfig
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
    def rule(self):
        '''Cluster-wide rules.
        '''
        return self.data['rule']

