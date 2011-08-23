
================================================================================
PhysicalNicCdpInfo
================================================================================


.. describe:: Property of
    
    :py:class:`~pyvisdk.do.physical_nic_hint_info.PhysicalNicHintInfo`
    
.. describe:: See also
    
    :py:class:`~pyvisdk.do.physical_nic_cdp_device_capability.PhysicalNicCdpDeviceCapability`
    
.. describe:: Since
    
    VI API 2.5
    
.. describe:: Extends
    
    :py:class:`~pyvisdk.mo.dynamic_data.DynamicData`
    
.. class:: pyvisdk.do.physical_nic_cdp_info.PhysicalNicCdpInfo
    
    .. py:attribute:: address
    
        The advertised IP address that is assigned to the interface of the device on which the CDP message is sent. The device can advertise all addresses for a given protocol suite and, optionally, can advertise one or more loopback IP addresses. But this property only show the first address.
        
    
    .. py:attribute:: cdpVersion
    
        CDP version. The value is always 1.
        
    
    .. py:attribute:: deviceCapability
    
        Device Capability PhysicalNicCdpDeviceCapability
        
    
    .. py:attribute:: devId
    
        Device ID which identifies the device. By default, the device ID is either the device's fully-qualified host name (including the domain name) or the device's hardware serial number in ASCII.
        
    
    .. py:attribute:: fullDuplex
    
        Half/full duplex setting of the advertising port.
        
    
    .. py:attribute:: hardwarePlatform
    
        Hardware platform. An ASCII character string that describes the hardware platform of the device , e.g. "cisco WS-C2940-8TT-S"
        
    
    .. py:attribute:: ipPrefix
    
        IP prefix. Each IP prefix represents one of the directly connected IP network segments of the local route.
        
    
    .. py:attribute:: ipPrefixLen
    
        ipPrefix length.
        
    
    .. py:attribute:: location
    
        The configured location of the device.
        
    
    .. py:attribute:: mgmtAddr
    
        The configured IP address of the SNMP management interface for the device.
        
    
    .. py:attribute:: mtu
    
        MTU, the maximum transmission unit for the advertising port. Possible values are 1500 through 18190.
        
    
    .. py:attribute:: portId
    
        Port ID. An ASCII character string that identifies the port on which the CDP message is sent, e.g. "FastEthernet0/8"
        
    
    .. py:attribute:: samples
    
        The number of CDP messages we have received from the device.
        
    
    .. py:attribute:: softwareVersion
    
        Software version on the device. A character string that provides information about the software release version that the device is running. e.g. "Cisco Internetwork Operating Syscisco WS-C2940-8TT-S"
        
    
    .. py:attribute:: systemName
    
        The configured SNMP system name of the device.
        
    
    .. py:attribute:: systemOID
    
        The configured SNMP system OID of the device.
        
    
    .. py:attribute:: timeout
    
        This is the periodicity of advertisement, the time between two successive CDP message transmissions
        
    
    .. py:attribute:: ttl
    
        Time-To-Live. the amount of time, in seconds, that a receiver should retain the information contained in the CDP packet.
        
    
    .. py:attribute:: vlan
    
        The native VLAN of advertising port. The native VLAN is the VLAN to which a port returns when it is not trunking. Also, the native VLAN is the untagged VLAN on an 802.1Q trunk.
        
    