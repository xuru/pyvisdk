
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVPortgroupConfigSpec(DynamicData):
    '''Specification to reconfigure a DistributedVirtualPortgroup.
    '''
    
    def __init__(self, configVersion, defaultPortConfig, description, name, numPorts, policy, portNameFormat, scope, type, vendorSpecificConfig):
        # MUST define these
        super(DVPortgroupConfigSpec, self).__init__()
    
        self.data['configVersion'] = configVersion
        self.data['defaultPortConfig'] = defaultPortConfig
        self.data['description'] = description
        self.data['name'] = name
        self.data['numPorts'] = numPorts
        self.data['policy'] = policy
        self.data['portNameFormat'] = portNameFormat
        self.data['scope'] = scope
        self.data['type'] = type
        self.data['vendorSpecificConfig'] = vendorSpecificConfig
    
    
    @property
    def configVersion(self):
        '''The version string of the configuration that this spec is trying to change. This
        property is required in reconfiguring a portgroup and should be set to the
        same value as the configVersion. This property is ignored in creating a
        portgroup if set.
        '''
        return self.data['configVersion']

    @property
    def defaultPortConfig(self):
        '''The default network setting for all the ports in the portgroup.
        '''
        return self.data['defaultPortConfig']

    @property
    def description(self):
        '''A description string of the portgroup.
        '''
        return self.data['description']

    @property
    def name(self):
        '''The name of the portgroup.
        '''
        return self.data['name']

    @property
    def numPorts(self):
        '''Number of ports in the portgroup. Setting this number larger than the number of
        existing ports in the portgroup causes new ports to be added to the
        portgroup to meet the number. Setting this property smaller than the
        number of existing ports deletes the free ports from the portgroup. If the
        number cannot be met by deleting free ports, a fault is raised. If new
        ports are added to the portgroup, they are also added to the switch. For
        portgroups of type ephemeral this property is ignored.
        '''
        return self.data['numPorts']

    @property
    def policy(self):
        '''Portgroup policy.
        '''
        return self.data['policy']

    @property
    def portNameFormat(self):
        '''The format of the name of the ports when ports are created in the portgroup. For
        details see portNameFormat.
        '''
        return self.data['portNameFormat']

    @property
    def scope(self):
        '''The eligible entities that can connects to the port, for detail see scope.
        '''
        return self.data['scope']

    @property
    def type(self):
        '''The type of portgroup. See DistributedVirtualPortgroupPortgroupType for possible
        values.
        '''
        return self.data['type']

    @property
    def vendorSpecificConfig(self):
        '''An opaque binary blob that stores vendor specific configuration.
        '''
        return self.data['vendorSpecificConfig']

