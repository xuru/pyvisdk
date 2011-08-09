
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitchPortConnection(DynamicData):
    '''The class that represents a connection or an association between
        DistributedVirtualPort and a vNIC or pNIC.
    '''
    
    def __init__(self, connectionCookie, portgroupKey, portKey, switchUuid):
        # MUST define these
        super(DistributedVirtualSwitchPortConnection, self).__init__()
    
        self.data['connectionCookie'] = connectionCookie
        self.data['portgroupKey'] = portgroupKey
        self.data['portKey'] = portKey
        self.data['switchUuid'] = switchUuid
    
    
    @property
    def connectionCookie(self):
        '''The cookie that represents this portConnection instance for the port. The value of
        this property is generated from the implementation. Any value set in a
        reconfiguring operation is ignored.
        '''
        return self.data['connectionCookie']

    @property
    def portgroupKey(self):
        '''The key of portgroup. If specified, this object represents a connection or an
        association between a DistributedVirtualPortgroup and a vNIC/pNIC. In this
        case, setting of portKey is not necessary for a early-binding portgroup
        and is not allowed for a late-binding portgroup. The portKey property will
        be populated by the implementation at the time of port binding.
        '''
        return self.data['portgroupKey']

    @property
    def portKey(self):
        '''The key of the port. If specified, this object represents a connection or an
        association between an individual DistributedVirtualPort and a vNIC/pNIC.
        See portgroupKey for more information on populating this property.
        '''
        return self.data['portKey']

    @property
    def switchUuid(self):
        '''The UUID of the switch.
        '''
        return self.data['switchUuid']

