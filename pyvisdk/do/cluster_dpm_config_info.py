
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterDpmConfigInfo(vim, *args, **kwargs):
    '''Configuration of the VMware DPM service.All fields are defined as optional. In
    case of a reconfiguration, unset fields are not changed.'''
    
    obj = vim.client.factory.create('ns0:ClusterDpmConfigInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'defaultDpmBehavior', 'enabled', 'hostPowerActionRate', 'option',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    