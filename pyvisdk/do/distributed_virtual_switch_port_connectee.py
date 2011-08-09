
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitchPortConnectee(DynamicData):
    '''Information about the entity that connects to a DistributedVirtualPort.
    '''
    
    def __init__(self, addressHint, connectedEntity, nicKey, type):
        # MUST define these
        super(DistributedVirtualSwitchPortConnectee, self).__init__()
    
        self.data['addressHint'] = addressHint
        self.data['connectedEntity'] = connectedEntity
        self.data['nicKey'] = nicKey
        self.data['type'] = type
    
    
    @property
    def addressHint(self):
        '''A hint on address information of the NIC that connects to this port.
        '''
        return self.data['addressHint']

    @property
    def connectedEntity(self):
        '''The connected entity. This property should always be set unless the user's setting
        does not have System.Read privilege on the object referred to by this
        property.
        '''
        return self.data['connectedEntity']

    @property
    def nicKey(self):
        '''The key of the virtual NIC that connects to this port.
        '''
        return self.data['nicKey']

    @property
    def type(self):
        '''The type of the connectee. See ConnecteeType for valid values.
        '''
        return self.data['type']

