
from pyvisdk.do.apply_profile import ApplyProfile
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class IpRouteProfile(ApplyProfile):
    '''DataObject representing the Ip Route configuration.
    '''
    
    def __init__(self, staticRoute):
        # MUST define these
        super(IpRouteProfile, self).__init__()
    
        self.data['staticRoute'] = staticRoute
    
    
    @property
    def staticRoute(self):
        '''Static routes that need to be configured
        '''
        return self.data['staticRoute']

