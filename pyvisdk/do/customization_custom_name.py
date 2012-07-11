
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationCustomName(vim, *args, **kwargs):
    '''Specifies that the VirtualCenter server will launch an external application to
    generate the (hostname/IP). The command line for this application must be
    specified in the server configuration file (vpxd.cfg) in the vpxd/name-ip-
    generator key.'''
    
    obj = vim.client.factory.create('ns0:CustomizationCustomName')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'argument', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    