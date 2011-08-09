
from pyvisdk.do.cluster_profile_config_spec import ClusterProfileConfigSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterProfileCompleteConfigSpec(ClusterProfileConfigSpec):
    '''DataObject completely specifying the configuration of the profile.
    '''
    
    def __init__(self, complyProfile):
        # MUST define these
        super(ClusterProfileCompleteConfigSpec, self).__init__()
    
        self.data['complyProfile'] = complyProfile
    
    
    @property
    def complyProfile(self):
        '''User defined compliance profile for the cluster. If unset, clear the
        complyProfile.
        '''
        return self.data['complyProfile']

