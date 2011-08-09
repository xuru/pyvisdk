
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVPortgroupConfigInfo(DynamicData):
    '''Configuration of a DistributedVirtualPortgroup.
    '''
    
    def __init__(self, configVersion, defaultPortConfig, description, distributedVirtualSwitch, key, name, numPorts, policy, portNameFormat, scope, type, vendorSpecificConfig):
        # MUST define these
        super(DVPortgroupConfigInfo, self).__init__()
    
        self.data['configVersion'] = configVersion
        self.data['defaultPortConfig'] = defaultPortConfig
        self.data['description'] = description
        self.data['distributedVirtualSwitch'] = distributedVirtualSwitch
        self.data['key'] = key
        self.data['name'] = name
        self.data['numPorts'] = numPorts
        self.data['policy'] = policy
        self.data['portNameFormat'] = portNameFormat
        self.data['scope'] = scope
        self.data['type'] = type
        self.data['vendorSpecificConfig'] = vendorSpecificConfig
    
    
    @property
    def configVersion(self):
        '''The version string of the configuration.
        '''
        return self.data['configVersion']

    @property
    def defaultPortConfig(self):
        '''The common network setting for all the ports in the portgroup.
        '''
        return self.data['defaultPortConfig']

    @property
    def description(self):
        '''A description string of the portgroup.
        '''
        return self.data['description']

    @property
    def distributedVirtualSwitch(self):
        '''The DistributedVirtualSwitch that the portgroup is defined on. This property
        should always be set unless the user's setting does not have System.Read
        privilege on the object referred to by this property.
        '''
        return self.data['distributedVirtualSwitch']

    @property
    def key(self):
        '''The key of the portgroup.
        '''
        return self.data['key']

    @property
    def name(self):
        '''The name of the portgroup.
        '''
        return self.data['name']

    @property
    def numPorts(self):
        '''Number of ports in the portgroup.
        '''
        return self.data['numPorts']

    @property
    def policy(self):
        '''Portgroup policy.
        '''
        return self.data['policy']

    @property
    def portNameFormat(self):
        '''If set, a name will be automatically generated based on this format string for a
        port when it is created in or moved into the portgroup. The format string
        can contain meta tags that will be resolved to the corresponding values in
        generating a name, if applicable for the port at the time of name
        generation.
        '''
        return self.data['portNameFormat']

    @property
    def scope(self):
        '''The eligible entities that can connect to the portgroup. If unset, there is no
        restriction on which entity can connect to the portgroup. If set, only the
        entities in the specified list or their child entities are allowed to
        connect to the portgroup. If scopes are defined at both port and portgroup
        level, they are taken as an "AND" relationship. If such a relationship
        doesn't make sense, the reconfigure operation will raise an exception.
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

