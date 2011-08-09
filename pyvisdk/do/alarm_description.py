
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AlarmDescription(DynamicData):
    '''Static strings for alarms.
    '''
    
    def __init__(self, action, datastoreConnectionState, entityStatus, expr, hostSystemConnectionState, hostSystemPowerState, metricOperator, stateOperator, virtualMachineGuestHeartbeatStatus, virtualMachinePowerState):
        # MUST define these
        super(AlarmDescription, self).__init__()
    
        self.data['action'] = action
        self.data['datastoreConnectionState'] = datastoreConnectionState
        self.data['entityStatus'] = entityStatus
        self.data['expr'] = expr
        self.data['hostSystemConnectionState'] = hostSystemConnectionState
        self.data['hostSystemPowerState'] = hostSystemPowerState
        self.data['metricOperator'] = metricOperator
        self.data['stateOperator'] = stateOperator
        self.data['virtualMachineGuestHeartbeatStatus'] = virtualMachineGuestHeartbeatStatus
        self.data['virtualMachinePowerState'] = virtualMachinePowerState
    
    
    @property
    def action(self):
        '''Action class descriptions for an alarm.
        '''
        return self.data['action']

    @property
    def datastoreConnectionState(self):
        '''accessible and description
        '''
        return self.data['datastoreConnectionState']

    @property
    def entityStatus(self):
        '''ManagedEntity Status enum description
        '''
        return self.data['entityStatus']

    @property
    def expr(self):
        '''Descriptions of expression types for a trigger.
        '''
        return self.data['expr']

    @property
    def hostSystemConnectionState(self):
        '''Host System Connection State enum description
        '''
        return self.data['hostSystemConnectionState']

    @property
    def hostSystemPowerState(self):
        '''Host System Power State enum description
        '''
        return self.data['hostSystemPowerState']

    @property
    def metricOperator(self):
        '''MetricAlarmExpression Metric Operator enum description
        '''
        return self.data['metricOperator']

    @property
    def stateOperator(self):
        '''State Operator enum description
        '''
        return self.data['stateOperator']

    @property
    def virtualMachineGuestHeartbeatStatus(self):
        '''Guest Heartbeat Status enum description
        '''
        return self.data['virtualMachineGuestHeartbeatStatus']

    @property
    def virtualMachinePowerState(self):
        '''Virtual Machine Power State enum description
        '''
        return self.data['virtualMachinePowerState']

