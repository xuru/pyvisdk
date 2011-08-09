
from pyvisdk.do.cluster_action import ClusterAction
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterHostPowerAction(ClusterAction):
    '''Describes a single host power action.
    '''
    
    def __init__(self, cpuCapacityMHz, memCapacityMB, operationType, powerConsumptionWatt):
        # MUST define these
        super(ClusterHostPowerAction, self).__init__()
    
        self.data['cpuCapacityMHz'] = cpuCapacityMHz
        self.data['memCapacityMB'] = memCapacityMB
        self.data['operationType'] = operationType
        self.data['powerConsumptionWatt'] = powerConsumptionWatt
    
    
    @property
    def cpuCapacityMHz(self):
        '''CPU capacity of the host in units of MHz. In case of power-on action, this is the
        projected increase in the cluster's CPU capacity. In case of power off,
        this is the projected decrease in the cluster's CPU capacity.
        '''
        return self.data['cpuCapacityMHz']

    @property
    def memCapacityMB(self):
        '''Memory capacity of the host in units of MM. In case of power-on action, this is
        the projected increase in the cluster's memory capacity. In case of power
        off, this is the projected decrease in the cluster's memory capacity.
        '''
        return self.data['memCapacityMB']

    @property
    def operationType(self):
        '''Specify whether the action is power on or power off
        '''
        return self.data['operationType']

    @property
    def powerConsumptionWatt(self):
        '''Estimated power consumption of the host. In case of power-on, this is the
        projected increase in the cluster's power consumption. In case of power
        off, this is the projected decrease in the cluster's power consumption
        '''
        return self.data['powerConsumptionWatt']

