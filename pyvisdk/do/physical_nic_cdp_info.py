
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PhysicalNicCdpInfo(DynamicData):
    '''CDP (Cisco Discovery Protocol) is a link level protocol that allows for
        discovering the CDP-awared network hardware at either end of a DIRECT
        connection. It's only good for direct connection because CDP doesn't get
        forwarded through switches. It's a simple advertisement protocol which
        beacons information about the switch or host along with some port
        information. The CDP information allows ESX Server admins to know which
        Cisco switch port is connected to any given virtual switch uplink (PNIC).
    '''
    
    def __init__(self, address, cdpVersion, deviceCapability, devId, fullDuplex, hardwarePlatform, ipPrefix, ipPrefixLen, location, mgmtAddr, mtu, portId, samples, softwareVersion, systemName, systemOID, timeout, ttl, vlan):
        # MUST define these
        super(PhysicalNicCdpInfo, self).__init__()
    
        self.data['address'] = address
        self.data['cdpVersion'] = cdpVersion
        self.data['deviceCapability'] = deviceCapability
        self.data['devId'] = devId
        self.data['fullDuplex'] = fullDuplex
        self.data['hardwarePlatform'] = hardwarePlatform
        self.data['ipPrefix'] = ipPrefix
        self.data['ipPrefixLen'] = ipPrefixLen
        self.data['location'] = location
        self.data['mgmtAddr'] = mgmtAddr
        self.data['mtu'] = mtu
        self.data['portId'] = portId
        self.data['samples'] = samples
        self.data['softwareVersion'] = softwareVersion
        self.data['systemName'] = systemName
        self.data['systemOID'] = systemOID
        self.data['timeout'] = timeout
        self.data['ttl'] = ttl
        self.data['vlan'] = vlan
    
    
    @property
    def address(self):
        '''The advertised IP address that is assigned to the interface of the device on which
        the CDP message is sent. The device can advertise all addresses for a
        given protocol suite and, optionally, can advertise one or more loopback
        IP addresses. But this property only show the first address.
        '''
        return self.data['address']

    @property
    def cdpVersion(self):
        '''CDP version. The value is always 1.
        '''
        return self.data['cdpVersion']

    @property
    def deviceCapability(self):
        '''Device Capability PhysicalNicCdpDeviceCapability
        '''
        return self.data['deviceCapability']

    @property
    def devId(self):
        '''Device ID which identifies the device. By default, the device ID is either the
        device's fully-qualified host name (including the domain name) or the
        device's hardware serial number in ASCII.
        '''
        return self.data['devId']

    @property
    def fullDuplex(self):
        '''Half/full duplex setting of the advertising port.
        '''
        return self.data['fullDuplex']

    @property
    def hardwarePlatform(self):
        '''Hardware platform. An ASCII character string that describes the hardware platform
        of the device , e.g. "cisco WS-C2940-8TT-S"
        '''
        return self.data['hardwarePlatform']

    @property
    def ipPrefix(self):
        '''IP prefix. Each IP prefix represents one of the directly connected IP network
        segments of the local route.
        '''
        return self.data['ipPrefix']

    @property
    def ipPrefixLen(self):
        '''ipPrefix length.
        '''
        return self.data['ipPrefixLen']

    @property
    def location(self):
        '''The configured location of the device.
        '''
        return self.data['location']

    @property
    def mgmtAddr(self):
        '''The configured IP address of the SNMP management interface for the device.
        '''
        return self.data['mgmtAddr']

    @property
    def mtu(self):
        '''MTU, the maximum transmission unit for the advertising port. Possible values are
        1500 through 18190.
        '''
        return self.data['mtu']

    @property
    def portId(self):
        '''Port ID. An ASCII character string that identifies the port on which the CDP
        message is sent, e.g. "FastEthernet0/8"
        '''
        return self.data['portId']

    @property
    def samples(self):
        '''The number of CDP messages we have received from the device.
        '''
        return self.data['samples']

    @property
    def softwareVersion(self):
        '''Software version on the device. A character string that provides information about
        the software release version that the device is running. e.g. "Cisco
        Internetwork Operating Syscisco WS-C2940-8TT-S"
        '''
        return self.data['softwareVersion']

    @property
    def systemName(self):
        '''The configured SNMP system name of the device.
        '''
        return self.data['systemName']

    @property
    def systemOID(self):
        '''The configured SNMP system OID of the device.
        '''
        return self.data['systemOID']

    @property
    def timeout(self):
        '''This is the periodicity of advertisement, the time between two successive CDP
        message transmissions
        '''
        return self.data['timeout']

    @property
    def ttl(self):
        '''Time-To-Live. the amount of time, in seconds, that a receiver should retain the
        information contained in the CDP packet.
        '''
        return self.data['ttl']

    @property
    def vlan(self):
        '''The native VLAN of advertising port. The native VLAN is the VLAN to which a port
        returns when it is not trunking. Also, the native VLAN is the untagged
        VLAN on an 802.1Q trunk.
        '''
        return self.data['vlan']

