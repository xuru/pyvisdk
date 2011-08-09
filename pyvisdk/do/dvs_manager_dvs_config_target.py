
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVSManagerDvsConfigTarget(DynamicData):
    '''Configuration specification for a DistributedVirtualSwitch or
        DistributedVirtualPortgroup.
    '''
    
    def __init__(self, distributedVirtualPortgroup, distributedVirtualSwitch):
        # MUST define these
        super(DVSManagerDvsConfigTarget, self).__init__()
    
        self.data['distributedVirtualPortgroup'] = distributedVirtualPortgroup
        self.data['distributedVirtualSwitch'] = distributedVirtualSwitch
    
    
    @property
    def distributedVirtualPortgroup(self):
        '''List of any DistributedVirtualPortgroup available for host vNIC connection.
        '''
        return self.data['distributedVirtualPortgroup']

    @property
    def distributedVirtualSwitch(self):
        '''List of any DistributedVirtualSwitch available for host vNIC connection.
        '''
        return self.data['distributedVirtualSwitch']

