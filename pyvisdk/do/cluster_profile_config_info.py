
from pyvisdk.do.profile_config_info import ProfileConfigInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterProfileConfigInfo(ProfileConfigInfo):
    '''
    '''
    
    def __init__(self, complyProfile):
        # MUST define these
        super(ClusterProfileConfigInfo, self).__init__()
    
        self.data['complyProfile'] = complyProfile
    
    
    @property
    def complyProfile(self):
        '''Compliance profile for the cluster
        '''
        return self.data['complyProfile']

