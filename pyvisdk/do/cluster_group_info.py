
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterGroupInfo(DynamicData):
    '''ClusterGroupInfo is the base type for all virtual machine and host groups. All
        virtual machines and hosts that are part of a group must be part of the
        same cluster.
    '''
    
    def __init__(self, name):
        # MUST define these
        super(ClusterGroupInfo, self).__init__()
    
        self.data['name'] = name
    
    
    @property
    def name(self):
        '''Unique name of the group.
        '''
        return self.data['name']

