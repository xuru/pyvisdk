
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterDrsConfigInfo(DynamicData):
    '''The ClusterDrsConfigInfo data object contains configuration information for the
        VMware DRS service.All fields are optional. If you set the parameter to
        when you call ReconfigureComputeResource_Task, an unset property has no
        effect on the existing property value in the cluster configuration on the
        Server. If you set the parameter to when you reconfigure a cluster, the
        cluster configuration is reverted to the default values, then the new
        configuration values are applied.
    '''
    
    def __init__(self, defaultVmBehavior, enabled, enableVmBehaviorOverrides, option, vmotionRate):
        # MUST define these
        super(ClusterDrsConfigInfo, self).__init__()
    
        self.data['defaultVmBehavior'] = defaultVmBehavior
        self.data['enabled'] = enabled
        self.data['enableVmBehaviorOverrides'] = enableVmBehaviorOverrides
        self.data['option'] = option
        self.data['vmotionRate'] = vmotionRate
    
    
    @property
    def defaultVmBehavior(self):
        '''Specifies the cluster-wide default DRS behavior for virtual machines. You can
        override the default behavior for a virtual machine by using the
        ClusterDrsVmConfigInfo object.
        '''
        return self.data['defaultVmBehavior']

    @property
    def enabled(self):
        '''Flag indicating whether or not the service is enabled.
        '''
        return self.data['enabled']

    @property
    def enableVmBehaviorOverrides(self):
        '''Flag that dictates whether DRS Behavior overrides for individual virtual machines
        (ClusterDrsVmConfigInfo) are enabled. The default value is
        '''
        return self.data['enableVmBehaviorOverrides']

    @property
    def option(self):
        '''Advanced settings.
        '''
        return self.data['option']

    @property
    def vmotionRate(self):
        '''Threshold for generated ClusterRecommendations. DRS generates only those
        recommendations that are above the specified vmotionRate. Ratings vary
        from 1 to 5. This setting applies to manual, partiallyAutomated, and
        fullyAutomated DRS clusters. See DrsBehavior.
        '''
        return self.data['vmotionRate']

