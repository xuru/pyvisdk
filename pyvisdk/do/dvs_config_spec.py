
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVSConfigSpec(DynamicData):
    '''Specification to reconfigure a DistributedVirtualSwitch.
    '''
    
    def __init__(self, configVersion, contact, defaultPortConfig, description, extensionKey, host, maxPorts, name, numStandalonePorts, policy, uplinkPortgroup, uplinkPortPolicy, vendorSpecificConfig):
        # MUST define these
        super(DVSConfigSpec, self).__init__()
    
        self.data['configVersion'] = configVersion
        self.data['contact'] = contact
        self.data['defaultPortConfig'] = defaultPortConfig
        self.data['description'] = description
        self.data['extensionKey'] = extensionKey
        self.data['host'] = host
        self.data['maxPorts'] = maxPorts
        self.data['name'] = name
        self.data['numStandalonePorts'] = numStandalonePorts
        self.data['policy'] = policy
        self.data['uplinkPortgroup'] = uplinkPortgroup
        self.data['uplinkPortPolicy'] = uplinkPortPolicy
        self.data['vendorSpecificConfig'] = vendorSpecificConfig
    
    
    @property
    def configVersion(self):
        '''The version string of the configuration that this spec is trying to change. This
        property is required in reconfiguring a switch and should be set to the
        same value as configVersion. This property is ignored during switch
        creation.
        '''
        return self.data['configVersion']

    @property
    def contact(self):
        '''Set the human operator contact information.
        '''
        return self.data['contact']

    @property
    def defaultPortConfig(self):
        '''The default configuration for ports.
        '''
        return self.data['defaultPortConfig']

    @property
    def description(self):
        '''Set the description string of the switch.
        '''
        return self.data['description']

    @property
    def extensionKey(self):
        '''The key of the extension registered by a remote server that controls the switch.
        '''
        return self.data['extensionKey']

    @property
    def host(self):
        '''The host member specification. A host should have only one entry in this array.
        Duplicate entries for the same host will raise a fault.
        '''
        return self.data['host']

    @property
    def maxPorts(self):
        '''The maximum number of DistributedVirtualPorts allowed in the switch. If specified
        in a reconfigure operation, this number cannot be smaller than the number
        of existing DistributedVirtualPorts.
        '''
        return self.data['maxPorts']

    @property
    def name(self):
        '''The name of the switch. Must be unique in the parent folder.
        '''
        return self.data['name']

    @property
    def numStandalonePorts(self):
        '''The number of standalone ports in the switch. Standalone ports are ports that do
        not belong to any portgroup. If set to a number larger than number of
        existing standalone ports in the switch, new ports get created to meet the
        number. If set to a number smaller than the number of existing standalone
        ports, free ports (uplink ports excluded) are deleted to meet the number.
        If the set number cannot be met by deleting free standalone ports, a fault
        is raised.
        '''
        return self.data['numStandalonePorts']

    @property
    def policy(self):
        '''The usage policy of the switch.
        '''
        return self.data['policy']

    @property
    def uplinkPortgroup(self):
        '''The uplink portgroups.
        '''
        return self.data['uplinkPortgroup']

    @property
    def uplinkPortPolicy(self):
        '''The uplink port policy.
        '''
        return self.data['uplinkPortPolicy']

    @property
    def vendorSpecificConfig(self):
        '''Set the opaque blob that stores vendor specific configuration.
        '''
        return self.data['vendorSpecificConfig']

