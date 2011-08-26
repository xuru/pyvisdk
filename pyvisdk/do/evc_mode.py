
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def EVCMode(vim, *args, **kwargs):
    '''When you add a host to an EVC-enabled cluster, the vCenter Server determines
    the CPU compatibility to preserve vMotion compatibility within the cluster. If
    the host CPU is compatible with those already in the cluster, the Server adds
    the host to the cluster and configures it for compatible operation. Hosts that
    are not compatible are not allowed to join the cluster.The inherited key
    property is a string value that uniquely identifies an EVC mode. The vCenter
    Server assigns the key value; the vSphere API uses the key to identify modes in
    summary and information objects: *
    ClusterComputeResourceSummary.currentEVCModeKey *
    HostListSummary.currentEVCModeKey * HostListSummary.maxEVCModeKey *
    VirtualMachineRuntimeInfo.minRequiredEVCModeKeyThe inherited label and summary
    properties are human-readable strings.You can use the track and vendorTier
    properties to determine feature-superset relationships between modes without
    examining the individual feature bits in guaranteedCPUFeatures. The CPU feature
    baseline of mode A is a superset of mode B's baseline if and only if: *
    modeA.track is the same as or a superset of modeB.track * modeA.vendorTier is
    equal to or greater than modeB.vendorTier Use the track and vendorTier
    properties only for the purpose of feature-superset calculations as described
    above. Do not use them to infer the presence or absence of specific features.
    The property values for a given mode may change across releases as the set of
    available EVC modes changes, to better represent mode relationships.'''
    
    obj = vim.client.factory.create('ns0:EVCMode')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 7 arguments got: %d' % len(args))
        
    signature = [ 'label', 'summary', 'key', 'track', 'vendor', 'vendorTier' ]
    inherited = [ 'guaranteedCPUFeatures' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    