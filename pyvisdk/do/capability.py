
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class Capability(DynamicData):
    '''A particular product may or may not support certain features. This data object
        indicates whether or not a service instance implements these features.
        This data object type indicates the circumstances under which an operation
        throws a NotSupported fault.Support for some features is indicated by the
        presence or absence of the manager object from the service instance. For
        example, the AlarmManager manager object indicates collecting alarms is
        supported. Other features indicate whether or not a given operation on an
        object throws a NotSupported fault.Some capabilities depend on the host or
        virtual machine version. These are specified by using the
        vim.host.Capability and vim.vm.Capability objects.
    '''
    
    def __init__(self, multiHostSupported, provisioningSupported, supportedEVCMode, userShellAccessSupported):
        # MUST define these
        super(Capability, self).__init__()
    
        self.data['multiHostSupported'] = multiHostSupported
        self.data['provisioningSupported'] = provisioningSupported
        self.data['supportedEVCMode'] = supportedEVCMode
        self.data['userShellAccessSupported'] = userShellAccessSupported
    
    
    @property
    def multiHostSupported(self):
        '''Indicates whether or not the service instance supports multiple hosts.
        '''
        return self.data['multiHostSupported']

    @property
    def provisioningSupported(self):
        '''Indicates whether or not the service instance supports provisioning. For example,
        the CloneVM operation.
        '''
        return self.data['provisioningSupported']

    @property
    def supportedEVCMode(self):
        '''All supported Enhanced VMotion Compatibility modes.
        '''
        return self.data['supportedEVCMode']

    @property
    def userShellAccessSupported(self):
        '''Flag indicating whether host user accounts should have the option to be granted
        shell access
        '''
        return self.data['userShellAccessSupported']

