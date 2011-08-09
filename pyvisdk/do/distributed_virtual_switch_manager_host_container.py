
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitchManagerHostContainer(DynamicData):
    '''Check host compatibility for all hosts in the container. If the recursive flag is
        true, then check hosts at all levels within this container, otherwise
        check only at the container level. In case of container being a
        Datacenter, the recursive flag is applied to its HostFolder.
    '''
    
    def __init__(self, container, recursive):
        # MUST define these
        super(DistributedVirtualSwitchManagerHostContainer, self).__init__()
    
        self.data['container'] = container
        self.data['recursive'] = recursive
    
    
    @property
    def container(self):
        '''Check compatibility of hosts in this container. The supported container types are
        Datacenter, Folder, and ComputeResource.
        '''
        return self.data['container']

    @property
    def recursive(self):
        '''If true, include hosts of all levels in the hierarchy with container as root of
        the tree. In case of container being a Datacenter, the recursive flag is
        applied to its HostFolder.
        '''
        return self.data['recursive']

