
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class IpPoolManager(BaseEntity):
    '''Singleton Managed Object used to manage IP Pools.IP Pools are used to allocate
    IPv4 and IPv6 addresses to vApps.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.IpPoolManager):
        super(IpPoolManager, self).__init__(core, name=name, ref=ref, type=type)

    

    
    
    def CreateIpPool(self, dc, pool):
        '''Create a new IP pool.Create a new IP pool.Create a new IP pool.
        
        :param dc: The datacenter on which to create the pool.
        
        :param pool: The IP pool to create on the server
        
        '''
        return self.delegate("CreateIpPool")(dc, pool)
    
    def DestroyIpPool(self, dc, id, force):
        '''Destroys an IP pool on the given datacenter.Destroys an IP pool on the given
        datacenter.
        
        :param dc: The datacenter on which to find the pool
        
        :param id: The unique ID of the pool
        
        :param force: If true, the pool will be destroyed even if it is in use
        
        '''
        return self.delegate("DestroyIpPool")(dc, id, force)
    
    def QueryIpPools(self, dc):
        '''Return the list of IP pools for a datacenter.
        
        :param dc: The datacenter for which to look up the IP pools.
        
        '''
        return self.delegate("QueryIpPools")(dc)
    
    def UpdateIpPool(self, dc, pool):
        '''Update an IP pool on a datacenter.Update an IP pool on a datacenter.Update an
        IP pool on a datacenter.
        
        :param dc: The datacenter on which to look up the pool.
        
        :param pool: The IP pool to update on the server
        
        '''
        return self.delegate("UpdateIpPool")(dc, pool)