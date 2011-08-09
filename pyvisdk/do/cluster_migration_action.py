
from pyvisdk.do.cluster_action import ClusterAction
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterMigrationAction(ClusterAction):
    '''Describes a single VM migration action.
    '''
    
    def __init__(self, drsMigration):
        # MUST define these
        super(ClusterMigrationAction, self).__init__()
    
        self.data['drsMigration'] = drsMigration
    
    
    @property
    def drsMigration(self):
        '''The details of the migration action
        '''
        return self.data['drsMigration']

