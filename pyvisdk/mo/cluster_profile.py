
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.profile import Profile

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterProfile(Profile):
    ''''''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.ClusterProfile):
        super(ClusterProfile, self).__init__(core, name=name, ref=ref, type=type)

    

    
    
    def UpdateClusterProfile(self, config):
        '''Update the ClusterProfile with the specified config.
        
        :param config: Specification which describes the changes.
        
        '''
        return self.delegate("UpdateClusterProfile")(config)