
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVSConfigInfo(DynamicData):
    '''Configuration of a DistributedVirtualSwitch.
    '''
    
    def __init__(self, configVersion, contact, createTime, defaultPortConfig, description, extensionKey, host, maxPorts, name, networkResourceManagementEnabled, numPorts, numStandalonePorts, policy, productInfo, targetInfo, uplinkPortgroup, uplinkPortPolicy, uuid, vendorSpecificConfig):
        # MUST define these
        super(DVSConfigInfo, self).__init__()
    
        self.data['configVersion'] = configVersion
        self.data['contact'] = contact
        self.data['createTime'] = createTime
        self.data['defaultPortConfig'] = defaultPortConfig
        self.data['description'] = description
        self.data['extensionKey'] = extensionKey
        self.data['host'] = host
        self.data['maxPorts'] = maxPorts
        self.data['name'] = name
        self.data['networkResourceManagementEnabled'] = networkResourceManagementEnabled
        self.data['numPorts'] = numPorts
        self.data['numStandalonePorts'] = numStandalonePorts
        self.data['policy'] = policy
        self.data['productInfo'] = productInfo
        self.data['targetInfo'] = targetInfo
        self.data['uplinkPortgroup'] = uplinkPortgroup
        self.data['uplinkPortPolicy'] = uplinkPortPolicy
        self.data['uuid'] = uuid
        self.data['vendorSpecificConfig'] = vendorSpecificConfig
    
    
    @property
    def configVersion(self):
        '''The version string of the configuration.
        '''
        return self.data['configVersion']

    @property
    def contact(self):
        '''The human operator contact information.
        '''
        return self.data['contact']

    @property
    def createTime(self):
        '''The create time of the switch.
        '''
        return self.data['createTime']

    @property
    def defaultPortConfig(self):
        '''The default configuration for the ports in the switch, if the port does not
        inherit configuration from the parent portgroup or has its own
        configuration.
        '''
        return self.data['defaultPortConfig']

    @property
    def description(self):
        '''A description string of the switch.
        '''
        return self.data['description']

    @property
    def extensionKey(self):
        '''The key of the extension registered by the remote server that controls the switch.
        '''
        return self.data['extensionKey']

    @property
    def host(self):
        '''The hosts that join the switch.
        '''
        return self.data['host']

    @property
    def maxPorts(self):
        '''The maximum number of ports allowed in the switch, not including conflict ports.
        '''
        return self.data['maxPorts']

    @property
    def name(self):
        '''The name of the switch.
        '''
        return self.data['name']

    @property
    def networkResourceManagementEnabled(self):
        '''Boolean to indicate if network I/O control is enabled on the switch.
        '''
        return self.data['networkResourceManagementEnabled']

    @property
    def numPorts(self):
        '''Current number of ports, not including conflict ports.
        '''
        return self.data['numPorts']

    @property
    def numStandalonePorts(self):
        '''The number of standalone ports in the switch. Standalone ports are ports that do
        not belong to any portgroup.
        '''
        return self.data['numStandalonePorts']

    @property
    def policy(self):
        '''The usage policy of the switch.
        '''
        return self.data['policy']

    @property
    def productInfo(self):
        '''The vendor, product, and version information for the implementation module of the
        switch.
        '''
        return self.data['productInfo']

    @property
    def targetInfo(self):
        '''The intended vendor, product, and version information for the implementation
        module of the switch.
        '''
        return self.data['targetInfo']

    @property
    def uplinkPortgroup(self):
        '''The uplink portgroups. When adding host members, a number of uplink ports, based
        on uplinkPortPolicy, are created for the host. If portgroups are shown
        here, those uplink ports will be added to the portgroups, with uplink
        ports evenly spread among the portgroups.
        '''
        return self.data['uplinkPortgroup']

    @property
    def uplinkPortPolicy(self):
        '''The uplink port policy.
        '''
        return self.data['uplinkPortPolicy']

    @property
    def uuid(self):
        '''The generated UUID of the switch. Unique across vCenter Server inventory and
        instances.
        '''
        return self.data['uuid']

    @property
    def vendorSpecificConfig(self):
        '''An opaque binary blob that stores vendor specific configuration.
        '''
        return self.data['vendorSpecificConfig']

