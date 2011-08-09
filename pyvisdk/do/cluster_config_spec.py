
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterConfigSpec(DynamicData):
    '''A complete cluster configuration. All fields are defined as optional. In case of a
        reconfiguration, unset fields are unchanged.
    '''
    
    def __init__(self, dasConfig, dasVmConfigSpec, drsConfig, drsVmConfigSpec, rulesSpec):
        # MUST define these
        super(ClusterConfigSpec, self).__init__()
    
        self.data['dasConfig'] = dasConfig
        self.data['dasVmConfigSpec'] = dasVmConfigSpec
        self.data['drsConfig'] = drsConfig
        self.data['drsVmConfigSpec'] = drsVmConfigSpec
        self.data['rulesSpec'] = rulesSpec
    
    
    @property
    def dasConfig(self):
        '''Changes to the configuration of VMware HA.
        '''
        return self.data['dasConfig']

    @property
    def dasVmConfigSpec(self):
        '''Changes to the per-virtual-machine VMware HA settings.
        '''
        return self.data['dasVmConfigSpec']

    @property
    def drsConfig(self):
        '''Changes to the configuration of the VMware DRS service.
        '''
        return self.data['drsConfig']

    @property
    def drsVmConfigSpec(self):
        '''Changes to the per-virtual-machine DRS settings.
        '''
        return self.data['drsVmConfigSpec']

    @property
    def rulesSpec(self):
        '''Changes to the set of rules.
        '''
        return self.data['rulesSpec']

