
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineConfigOptionDescriptor(DynamicData):
    '''Contains the definition of a unique key that can be used to retrieve a
        configOption object.
    '''
    
    def __init__(self, createSupported, defaultConfigOption, description, host, key):
        # MUST define these
        super(VirtualMachineConfigOptionDescriptor, self).__init__()
    
        self.data['createSupported'] = createSupported
        self.data['defaultConfigOption'] = defaultConfigOption
        self.data['description'] = description
        self.data['host'] = host
        self.data['key'] = key
    
    
    @property
    def createSupported(self):
        '''Indicates whether the associated set of configuration options can be used for
        virtual machine creation on a given host or cluster.
        '''
        return self.data['createSupported']

    @property
    def defaultConfigOption(self):
        '''Indicates whether the associated set of virtual machine configuration options is
        the default one for a given host or cluster. If this setting is TRUE,
        virtual machine creates will use the associated set of configuration
        options, unless a config version is explicitly specified in the
        ConfigSpec.
        '''
        return self.data['defaultConfigOption']

    @property
    def description(self):
        '''A description of the configOption object.
        '''
        return self.data['description']

    @property
    def host(self):
        '''List of hosts to which this descriptor applies.
        '''
        return self.data['host']

    @property
    def key(self):
        '''A unique key used to identify a configOption object in this EnvironmentBrowser.
        '''
        return self.data['key']

