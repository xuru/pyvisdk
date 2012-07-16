
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostFibreChannelOverEthernetTargetTransport(vim, *args, **kwargs):
    '''Fibre Channel Over Ethernet transport information about a SCSI target. FCoE
    transport information is that of: the regular FC World Wide Node and Port
    Names; the VNPort MAC address and FCF MAC address which constitute a VN_Port to
    VF_Port Virtual Link; and the VLAN on which an FCoE target resides. More FCoE
    information can be found in the working draft of the T11's Fibre Channel
    Backbone 5 standard (FC-BB-5). The draft can be found at http://www.t11.org.'''
    
    obj = vim.client.factory.create('ns0:HostFibreChannelOverEthernetTargetTransport')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'fcfMac', 'vlanId', 'vnportMac', 'nodeWorldWideName', 'portWorldWideName' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    