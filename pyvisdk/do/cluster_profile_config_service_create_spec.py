
from pyvisdk.do.cluster_profile_config_spec import ClusterProfileConfigSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterProfileConfigServiceCreateSpec(ClusterProfileConfigSpec):
    '''DataObject which allows reconfiguration of a profile based on services that will
        be available on the cluster.
    '''
    
    def __init__(self, serviceType):
        # MUST define these
        super(ClusterProfileConfigServiceCreateSpec, self).__init__()
    
        self.data['serviceType'] = serviceType
    
    
    @property
    def serviceType(self):
        '''Type of the service for which the ClusterProfile is being requested. If more than
        one service is specified, the created ClusterProfile will cater for all
        the services. Possible values are specified by ClusterProfileServiceType.
        If unset, clear the compliance expressions on the profile.
        '''
        return self.data['serviceType']

