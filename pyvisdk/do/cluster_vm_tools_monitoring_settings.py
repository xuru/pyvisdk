
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterVmToolsMonitoringSettings(DynamicData):
    '''VMware HA Virtual Machine Health Monitoring service setting.Virtual Machine Health
        Monitoring service checks the VMware Tools heartbeat of a virtual machine.
        If heartbeats have not been received within a specified time interval,
        Virtual Machine Health Monitoring service declares the virtual machine as
        failed and resets the virtual machine.VmToolsMonitoringSetting consists of
        configuration settings for Virtual Machine Health Monitoring Service.All
        fields are defined as optional. In case of a reconfiguration, fields left
        unset are not changed.
    '''
    
    def __init__(self, clusterSettings, enabled, failureInterval, maxFailures, maxFailureWindow, minUpTime, vmMonitoring):
        # MUST define these
        super(ClusterVmToolsMonitoringSettings, self).__init__()
    
        self.data['clusterSettings'] = clusterSettings
        self.data['enabled'] = enabled
        self.data['failureInterval'] = failureInterval
        self.data['maxFailures'] = maxFailures
        self.data['maxFailureWindow'] = maxFailureWindow
        self.data['minUpTime'] = minUpTime
        self.data['vmMonitoring'] = vmMonitoring
    
    
    @property
    def clusterSettings(self):
        '''Flag indicating whether to use the cluster settings or the per VM settings
        '''
        return self.data['clusterSettings']

    @property
    def enabled(self):
        '''Flag indicating whether or not the Virtual Machine Health Monitoring service is
        enabled.
        '''
        return self.data['enabled']

    @property
    def failureInterval(self):
        '''If no heartbeat has been received for at least the specified number of seconds,
        the virtual machine is declared as failed.
        '''
        return self.data['failureInterval']

    @property
    def maxFailures(self):
        '''Maximum number of failures and automated resets allowed during the time that
        maxFailureWindow specifies. If maxFailureWindow is -1 (no window), this
        represents the absolute number of failures after which automated response
        is stopped.
        '''
        return self.data['maxFailures']

    @property
    def maxFailureWindow(self):
        '''The number of seconds for the window during which up to maxFailures resets can
        occur before automated responses stop.
        '''
        return self.data['maxFailureWindow']

    @property
    def minUpTime(self):
        '''The number of seconds for the virtual machine's heartbeats to stabilize after the
        virtual machine has been powered on. This time should include the guest
        operating system boot-up time. The virtual machine monitoring will begin
        only after this period.
        '''
        return self.data['minUpTime']

    @property
    def vmMonitoring(self):
        '''Indicates the type of vm monitoring configured. This can be one fo three values
        disabled, vmMonitoringOnly or vmAndAppMonitoring The default value is
        vmMonitoringDisabled Please see ClusterDasConfigInfoVmMonitoringState
        '''
        return self.data['vmMonitoring']

