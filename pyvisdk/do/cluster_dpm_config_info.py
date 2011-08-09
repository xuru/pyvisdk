
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterDpmConfigInfo(DynamicData):
    '''Configuration of the VMware DPM service.All fields are defined as optional. In
        case of a reconfiguration, unset fields are not changed.
    '''
    
    def __init__(self, defaultDpmBehavior, enabled, hostPowerActionRate, option):
        # MUST define these
        super(ClusterDpmConfigInfo, self).__init__()
    
        self.data['defaultDpmBehavior'] = defaultDpmBehavior
        self.data['enabled'] = enabled
        self.data['hostPowerActionRate'] = hostPowerActionRate
        self.data['option'] = option
    
    
    @property
    def defaultDpmBehavior(self):
        '''Specifies the default VMware DPM behavior for hosts. This default behavior can be
        overridden on a per host basis using the ClusterDpmHostConfigInfo object.
        '''
        return self.data['defaultDpmBehavior']

    @property
    def enabled(self):
        '''Flag indicating whether or not the service is enabled. This service can not be
        enabled, unless DRS is enabled as well.
        '''
        return self.data['enabled']

    @property
    def hostPowerActionRate(self):
        '''DPM generates only those recommendations that are above the specified rating.
        Ratings vary from 1 to 5. This setting applies to both manual and
        automated (@link DpmBehavior) DPM clusters.
        '''
        return self.data['hostPowerActionRate']

    @property
    def option(self):
        '''Advanced settings.
        '''
        return self.data['option']

