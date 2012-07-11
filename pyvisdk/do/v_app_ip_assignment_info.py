
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VAppIPAssignmentInfo(vim, *args, **kwargs):
    '''The IPAssignmentInfo class specifies how the guest software gets configured
    with IP addresses, including protocol type (IPv4 or IPv6) and the life-time of
    those IP addresses.A vApp/virtual machine can either use DHCP to acquire an IP
    configuration, or it can acquire its IP configuration through the use of the VI
    platform using the OVF environment's properties. The latter is a known as OVF-
    environment-assigned IP configuration.Guest software can be constructed to
    support DHCP , OVF assigned IP configuration, or both. The
    supportedAssignmentScheme property lists the supported schemes. This is
    typically specified by the author of a vApp.The deployer / operator of a vApp,
    specifies what IP allocation policy should be used:* Using DHCP, if the vApp
    and deployed network supports it * Transient Assignment, if the vApp supports
    OVF-assigned IP configuration and the network has an IP range configured. *
    Fixed Assignment, if the vApp supports OVF-assigned IP configuration and the
    network has an IP range configured.Transient and fixed assignment differs in
    the life time of the IP allocation. For transient, IP addresses are
    automatically assigned on power-on and released on power-off. For a fixed, the
    IP addresses are explicitly specified by the deployer and does not change
    between a power-on/power-off.The IPAssignment settings are global to a
    deployment. Thus,if a vApp or virtual machine is part of another vApp, then the
    settings are ignored, and the ones for the top-most vApp container is used.'''
    
    obj = vim.client.factory.create('ns0:VAppIPAssignmentInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'ipAllocationPolicy', 'ipProtocol', 'supportedAllocationScheme',
        'supportedIpProtocol', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    