import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

def MOFactory(core, ref):
    log.debug("REF: %s" % ref)
    _class = eval("%s" % ref.obj._type)
    return _class(core,  name=ref.propSet[0].val, ref=ref.obj)

# managed entities
ManagedEntities = {
    "ManagedEntity": MOFactory,
    "ComputeResource": MOFactory,
    "ClusterComputeResource": MOFactory,
    "Datacenter": MOFactory,
    "Folder": MOFactory,
    "HostSystem": MOFactory,
    "ResourcePool": MOFactory,
    "VirtualMachine": MOFactory,
    "VirtualMachineSnapshot": MOFactory,
    "Datastore": MOFactory,
}

# compute resources
ComputeResources = {
    "ComputeResource": lambda x: ManagedObjectReference("ComputeResource", x),
    "ClusterComputeResource": lambda x: ManagedObjectReference("ClusterComputeResource", x),
}

# Collectors
HistoryCollectors = {
    "HistoryCollector": lambda x: ManagedObjectReference("HistoryCollector", x),
    "EventHistoryCollector": lambda x: ManagedObjectReference("EventHistoryCollector", x),
    "TaskHistoryCollector": lambda x: ManagedObjectReference("TaskHistoryCollector", x),
}


from datacenter import *
from datastore import *
from host import *
from pyvisdk.core import ManagedObjectReference
from snapshot import *
from vm import *


