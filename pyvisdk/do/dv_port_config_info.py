
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVPortConfigInfo(DynamicData):
    '''Management related configuration of a DistributedVirtualPort.
    '''
    
    def __init__(self, configVersion, description, name, scope, setting):
        # MUST define these
        super(DVPortConfigInfo, self).__init__()
    
        self.data['configVersion'] = configVersion
        self.data['description'] = description
        self.data['name'] = name
        self.data['scope'] = scope
        self.data['setting'] = setting
    
    
    @property
    def configVersion(self):
        '''The version string of the configuration.
        '''
        return self.data['configVersion']

    @property
    def description(self):
        '''A description string of the port.
        '''
        return self.data['description']

    @property
    def name(self):
        '''The name of the port.
        '''
        return self.data['name']

    @property
    def scope(self):
        '''The eligible entities that can connect to the port. If unset, there is no
        restriction on which entity can connect to the port. If set, only the
        entities in the specified list or their child entities are allowed to
        connect to the port. If scopes are defined at both port and portgroup
        level, they are taken as an "AND" relationship. If such a relationship
        doesn't make sense, the reconfigure operation will raise an exception.
        '''
        return self.data['scope']

    @property
    def setting(self):
        '''The network configuration of the port.
        '''
        return self.data['setting']

