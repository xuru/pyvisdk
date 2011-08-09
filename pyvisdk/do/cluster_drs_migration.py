
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterDrsMigration(DynamicData):
    '''Describes a single virtual machine migration.
    '''
    
    def __init__(self, cpuLoad, destination, destinationCpuLoad, destinationMemoryLoad, key, memoryLoad, source, sourceCpuLoad, sourceMemoryLoad, time, vm):
        # MUST define these
        super(ClusterDrsMigration, self).__init__()
    
        self.data['cpuLoad'] = cpuLoad
        self.data['destination'] = destination
        self.data['destinationCpuLoad'] = destinationCpuLoad
        self.data['destinationMemoryLoad'] = destinationMemoryLoad
        self.data['key'] = key
        self.data['memoryLoad'] = memoryLoad
        self.data['source'] = source
        self.data['sourceCpuLoad'] = sourceCpuLoad
        self.data['sourceMemoryLoad'] = sourceMemoryLoad
        self.data['time'] = time
        self.data['vm'] = vm
    
    
    @property
    def cpuLoad(self):
        '''Current CPU load for the virtual machine, in MHz. This property is only populated
        for recommendations.
        '''
        return self.data['cpuLoad']

    @property
    def destination(self):
        '''Destination host.
        '''
        return self.data['destination']

    @property
    def destinationCpuLoad(self):
        '''Current CPU load on the destination host, in MHz.
        '''
        return self.data['destinationCpuLoad']

    @property
    def destinationMemoryLoad(self):
        '''Current memory usage on the destination host, in bytes.
        '''
        return self.data['destinationMemoryLoad']

    @property
    def key(self):
        '''A unique key that identifies this recommendation. This is used as an argument to
        ComputeResource.applyRecommendation.
        '''
        return self.data['key']

    @property
    def memoryLoad(self):
        '''Current memory load for the virtual machine, in bytes. This field is only
        populated for recommendations.
        '''
        return self.data['memoryLoad']

    @property
    def source(self):
        '''Source host.
        '''
        return self.data['source']

    @property
    def sourceCpuLoad(self):
        '''Current CPU load on the source host, in MHz.
        '''
        return self.data['sourceCpuLoad']

    @property
    def sourceMemoryLoad(self):
        '''Current memory usage on the source host, in bytes.
        '''
        return self.data['sourceMemoryLoad']

    @property
    def time(self):
        '''The time this recommendation was computed.
        '''
        return self.data['time']

    @property
    def vm(self):
        '''The virtual machine selected for migration.
        '''
        return self.data['vm']

