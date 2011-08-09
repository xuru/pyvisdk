
from pyvisdk.do.cluster_action import ClusterAction
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterInitialPlacementAction(ClusterAction):
    '''Describes an initial placement of a single virtual machine
    '''
    
    def __init__(self, pool, targetHost):
        # MUST define these
        super(ClusterInitialPlacementAction, self).__init__()
    
        self.data['pool'] = pool
        self.data['targetHost'] = targetHost
    
    
    @property
    def pool(self):
        '''The resource pool to place the virtual machine into in case this action is for
        migrating from outside cluster.
        '''
        return self.data['pool']

    @property
    def targetHost(self):
        '''The host where the virtual machine should be initially placed.
        '''
        return self.data['targetHost']

