
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNatServiceSpec(DynamicData):
    '''This data object type provides the details about the Network Address Translation
        (NAT) service.
    '''
    
    def __init__(self, activeFtp, allowAnyOui, configPort, ipGatewayAddress, nameService, portForward, udpTimeout, virtualSwitch):
        # MUST define these
        super(HostNatServiceSpec, self).__init__()
    
        self.data['activeFtp'] = activeFtp
        self.data['allowAnyOui'] = allowAnyOui
        self.data['configPort'] = configPort
        self.data['ipGatewayAddress'] = ipGatewayAddress
        self.data['nameService'] = nameService
        self.data['portForward'] = portForward
        self.data['udpTimeout'] = udpTimeout
        self.data['virtualSwitch'] = virtualSwitch
    
    
    @property
    def activeFtp(self):
        '''The flag to indicate whether or not non-passive mode FTP connections should be
        allowed.
        '''
        return self.data['activeFtp']

    @property
    def allowAnyOui(self):
        '''The flag to indicate whether or not the NAT Service allows media access control
        traffic from any Organizational Unique Identifier (OUI)? By default, it
        does not allow traffic that originated from the host to avoid packet
        loops.
        '''
        return self.data['allowAnyOui']

    @property
    def configPort(self):
        '''The flag to indicate whether or not the NAT Service should open a configuration
        port.
        '''
        return self.data['configPort']

    @property
    def ipGatewayAddress(self):
        '''The IP address that the NAT Service should use on the virtual network.
        '''
        return self.data['ipGatewayAddress']

    @property
    def nameService(self):
        '''The configuration of naming services. These parameters are specific to Windows.
        '''
        return self.data['nameService']

    @property
    def portForward(self):
        '''The port forwarding specifications to allow network connections to be initiated
        from outside the firewall.
        '''
        return self.data['portForward']

    @property
    def udpTimeout(self):
        '''The time allotted for UDP packets.
        '''
        return self.data['udpTimeout']

    @property
    def virtualSwitch(self):
        '''The name of the virtual switch to which nat service is connected.
        '''
        return self.data['virtualSwitch']

