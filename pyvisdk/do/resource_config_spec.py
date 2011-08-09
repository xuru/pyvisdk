
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ResourceConfigSpec(DynamicData):
    '''This data object type is a specification for a set of resources allocated to a
        virtual machine or a resource pool.
    '''
    
    def __init__(self, changeVersion, cpuAllocation, entity, lastModified, memoryAllocation):
        # MUST define these
        super(ResourceConfigSpec, self).__init__()
    
        self.data['changeVersion'] = changeVersion
        self.data['cpuAllocation'] = cpuAllocation
        self.data['entity'] = entity
        self.data['lastModified'] = lastModified
        self.data['memoryAllocation'] = memoryAllocation
    
    
    @property
    def changeVersion(self):
        '''The changeVersion is a unique identifier for a given version of the configuration.
        Each change to the configuration will update this value. This is typically
        implemented as an ever increasing count or a time-stamp. However, a client
        should always treat this as an opaque string.
        '''
        return self.data['changeVersion']

    @property
    def cpuAllocation(self):
        '''Resource allocation for CPU.
        '''
        return self.data['cpuAllocation']

    @property
    def entity(self):
        '''Reference to the entity with this resource specification: either a VirtualMachine
        or a ResourcePool.
        '''
        return self.data['entity']

    @property
    def lastModified(self):
        '''Timestamp when the resources were last modified. This is ignored when the object
        is used to update a configuration.
        '''
        return self.data['lastModified']

    @property
    def memoryAllocation(self):
        '''Resource allocation for memory.
        '''
        return self.data['memoryAllocation']

