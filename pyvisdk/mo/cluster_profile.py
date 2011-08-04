
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.profile import Profile
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterProfile(Profile):
    '''Update the ClusterProfile with the specified config.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.ClusterProfile):
        # MUST define these
        super(ClusterProfile, self).__init__(core, name=name, ref=ref, type=type)
    
    
