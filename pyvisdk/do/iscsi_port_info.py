
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def IscsiPortInfo(vim, *args, **kwargs):
    '''The IscsiPortInfo data object describes the Virtual NIC that are bound to an
    iSCSI adapter and also it describes the candidate Virtual NICs that can be
    bound to a given iSCSI adapter.'''
    
    obj = vim.client.factory.create('ns0:IscsiPortInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'complianceStatus', 'pathStatus', 'pnic', 'pnicDevice', 'portgroupKey',
        'portgroupName', 'portKey', 'switchName', 'switchUuid', 'vnic', 'vnicDevice',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    