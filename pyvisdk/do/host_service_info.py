
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostServiceInfo(DynamicData):
    '''Data object describing the host service configuration.
    '''
    
    def __init__(self, service):
        # MUST define these
        super(HostServiceInfo, self).__init__()
    
        self.data['service'] = service
    
    
    @property
    def service(self):
        '''List of configured services.
        '''
        return self.data['service']

