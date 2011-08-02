
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.profile_manager import ProfileManager
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterProfileManager(ProfileManager):
    '''
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.ClusterProfileManager):
        # MUST define these
        super(ClusterProfileManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
