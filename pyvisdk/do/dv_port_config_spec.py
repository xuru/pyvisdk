
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVPortConfigSpec(DynamicData):
    '''Specification to reconfigure a DistributedVirtualPort.
    '''
    
    def __init__(self, configVersion, description, key, name, operation, scope, setting):
        # MUST define these
        super(DVPortConfigSpec, self).__init__()
    
        self.data['configVersion'] = configVersion
        self.data['description'] = description
        self.data['key'] = key
        self.data['name'] = name
        self.data['operation'] = operation
        self.data['scope'] = scope
        self.data['setting'] = setting
    
    
    @property
    def configVersion(self):
        '''The version string of the configuration.
        '''
        return self.data['configVersion']

    @property
    def description(self):
        '''The description string of the port.
        '''
        return self.data['description']

    @property
    def key(self):
        '''The key of the port to be reconfigured.
        '''
        return self.data['key']

    @property
    def name(self):
        '''The name of the port.
        '''
        return self.data['name']

    @property
    def operation(self):
        '''The operation to remove or modify the existing ports. The valid values are: * edit
        * remove
        '''
        return self.data['operation']

    @property
    def scope(self):
        '''The eligible entities that can connect to the port, for detail see scope.
        '''
        return self.data['scope']

    @property
    def setting(self):
        '''The network setting of the port.
        '''
        return self.data['setting']

