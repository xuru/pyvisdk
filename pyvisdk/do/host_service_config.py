
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostServiceConfig(DynamicData):
    '''DataObject representing configuration for a particular service.
    '''
    
    def __init__(self, serviceId, startupPolicy):
        # MUST define these
        super(HostServiceConfig, self).__init__()
    
        self.data['serviceId'] = serviceId
        self.data['startupPolicy'] = startupPolicy
    
    
    @property
    def serviceId(self):
        '''Key of the service to configure.
        '''
        return self.data['serviceId']

    @property
    def startupPolicy(self):
        '''Startup policy which defines how the service be configured. See
        '''
        return self.data['startupPolicy']

