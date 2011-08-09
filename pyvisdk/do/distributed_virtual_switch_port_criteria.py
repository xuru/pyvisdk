
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitchPortCriteria(DynamicData):
    '''The criteria specification for selecting ports.
    '''
    
    def __init__(self, active, connected, inside, portgroupKey, portKey, scope, uplinkPort):
        # MUST define these
        super(DistributedVirtualSwitchPortCriteria, self).__init__()
    
        self.data['active'] = active
        self.data['connected'] = connected
        self.data['inside'] = inside
        self.data['portgroupKey'] = portgroupKey
        self.data['portKey'] = portKey
        self.data['scope'] = scope
        self.data['uplinkPort'] = uplinkPort
    
    
    @property
    def active(self):
        '''If set, only the active ports are qualified.
        '''
        return self.data['active']

    @property
    def connected(self):
        '''If set, only the connected ports are qualified.
        '''
        return self.data['connected']

    @property
    def inside(self):
        '''If unset, all ports in the switch are qualified. If set to true, only ports inside
        portgroupKey or any portgroup, if not set, are qualified. If set to false,
        only ports outside portgroupKey or any portgroup, if not set, are
        qualified.
        '''
        return self.data['inside']

    @property
    def portgroupKey(self):
        '''The keys of the portgroup that is used for the scope of inside. If this property
        is unset, it means any portgroup. If inside is unset, this property is
        ignored.
        '''
        return self.data['portgroupKey']

    @property
    def portKey(self):
        '''If set, only the ports of which the key is in the array are qualified.
        '''
        return self.data['portKey']

    @property
    def scope(self):
        '''If set, only the ports of which the scope covers the entity are qualified.
        '''
        return self.data['scope']

    @property
    def uplinkPort(self):
        '''If set to true, only the uplink ports are qualified. If set to false, only non-
        uplink ports are qualified.
        '''
        return self.data['uplinkPort']

