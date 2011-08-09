
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPatchManagerStatusPrerequisitePatch(DynamicData):
    '''Updates that are required to be installed before this update can be installed on
        the server. In addition to being installed on the server, an update can
        have additional requirement on the server or services running on the
        server pertaining to the prerequisite update.
    '''
    
    def __init__(self, id, installState):
        # MUST define these
        super(HostPatchManagerStatusPrerequisitePatch, self).__init__()
    
        self.data['id'] = id
        self.data['installState'] = installState
    
    
    @property
    def id(self):
        '''Unique identifier of the prerequisite update.
        '''
        return self.data['id']

    @property
    def installState(self):
        '''The requirement on the server or services running on the server pertaining to the
        prerequisite update. For example, this update could require the server to
        be rebooted after the prerequisite update is installed. Unset if there is
        no additional requirement on the prerequisite update.
        '''
        return self.data['installState']

