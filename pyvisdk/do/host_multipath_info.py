
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostMultipathInfo(vim, *args, **kwargs):
    '''The HostMultipathInfo data object describes the multipathing policy
    configuration to determine the storage failover policies for a SCSI logical
    unit. The multipathing policy configuration operates on SCSI logical units and
    the paths to the logical units.Multipath policy configuration is only possible
    on storage devices provided by the native multipathing plug-store plugin.
    Storage devices using the native multipathing storage plugin will have an entry
    in this data object. Storage devices provided by a different storage plugin
    will not appear in the inventory represented by this data object.Legacy note:
    In hosts where HostMultipathStateInfo is not defined or does not exist on the
    HostStorageDeviceInfo object, only native multipathing exists. That means for
    these hosts, the MultipathInfo object contains the complete set of LUNs and
    paths on the LUNs available on the host.'''
    
    obj = vim.client.factory.create('ns0:HostMultipathInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'lun', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    