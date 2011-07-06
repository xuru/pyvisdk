import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

class PyVisdkError(Exception):
    pass

def MOFactory(core, ref):
    log.debug("REF: %s" % ref)
    
    # if we have an obj, then obj is the managed object reference
    if hasattr(ref, 'obj'):
        _class = eval("%s" % ref.obj._type)
        return _class(core,  name=ref.propSet[0].val, ref=ref.obj)
    
    # check if ref are the managed object reference
    elif (hasattr(ref, '_type') and hasattr(ref, 'value')) or ref.__class__.__name__ == 'ManagedObjectReference':
        _class = eval("%s" % ref._type)
        return _class(core,  ref=ref)
    
    # make sure we catch anything else...
    else:
        raise PyVisdkError("Unknown managed object reference: %s" % ref)

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
from folder import *
from pyvisdk.core import ManagedObjectReference
from snapshot import *
from vm import *


