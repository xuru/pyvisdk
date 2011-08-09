
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostUnresolvedVmfsVolumeResolveStatus(DynamicData):
    '''Data object that describes the resolvability of a volume.
    '''
    
    def __init__(self, incompleteExtents, multipleCopies, resolvable):
        # MUST define these
        super(HostUnresolvedVmfsVolumeResolveStatus, self).__init__()
    
        self.data['incompleteExtents'] = incompleteExtents
        self.data['multipleCopies'] = multipleCopies
        self.data['resolvable'] = resolvable
    
    
    @property
    def incompleteExtents(self):
        '''Is the list of extents for the volume a partial list? A volume can only be
        resignatured if all extents composing that volume are available. Hence, a
        volume with a partial extent list cannot be resignatured.
        '''
        return self.data['incompleteExtents']

    @property
    def multipleCopies(self):
        '''Are there multiple copies of extents for this volume? If any extent of the volume
        has multiple copies then the extents to be resolved must be explicitly
        specified when resolving this volume.
        '''
        return self.data['multipleCopies']

    @property
    def resolvable(self):
        '''Can this volume be resolved? There may be other reasons a volume cannot be
        resolved other than the fact that it is incomplete. This boolean will
        authoritatively indicate if the server can resolve this volume.
        '''
        return self.data['resolvable']

