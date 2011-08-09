
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VAppCloneSpec(DynamicData):
    '''Specification for a vApp cloning operation.
    '''
    
    def __init__(self, host, location, networkMapping, property, provisioning, resourceMapping, resourceSpec, vmFolder):
        # MUST define these
        super(VAppCloneSpec, self).__init__()
    
        self.data['host'] = host
        self.data['location'] = location
        self.data['networkMapping'] = networkMapping
        self.data['property'] = property
        self.data['provisioning'] = provisioning
        self.data['resourceMapping'] = resourceMapping
        self.data['resourceSpec'] = resourceSpec
        self.data['vmFolder'] = vmFolder
    
    
    @property
    def host(self):
        '''The target host for the virtual machines. This is often not a required parameter.
        If not specified, the behavior is as follows: * If the target pool
        represents a stand-alone host, that host is used. * If the target pool
        represents a DRS-enabled cluster, a host selected by DRS is used. * If the
        target pool represents a cluster without DRS enabled or a DRS-enabled
        cluster in manual mode, an InvalidArgument exception is thrown.
        '''
        return self.data['host']

    @property
    def location(self):
        '''Location where the destination vApp must be stored
        '''
        return self.data['location']

    @property
    def networkMapping(self):
        '''Network mappings. See NetworkMappingPair.
        '''
        return self.data['networkMapping']

    @property
    def property_(self):
        '''A set of property values to override.
        '''
        return self.data['property']

    @property
    def provisioning(self):
        '''Specify how the VMs in the vApp should be provisioned.
        '''
        return self.data['provisioning']

    @property
    def resourceMapping(self):
        '''The resource configuration for the cloned vApp.
        '''
        return self.data['resourceMapping']

    @property
    def resourceSpec(self):
        '''The resource configuration for the vApp.
        '''
        return self.data['resourceSpec']

    @property
    def vmFolder(self):
        '''The VM Folder to associate the vApp with
        '''
        return self.data['vmFolder']

