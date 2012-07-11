
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostConfigSpec(vim, *args, **kwargs):
    '''The HostConfigSpec data object provides access to data objects that specify
    configuration changes to be applied to an ESX host.'''
    
    obj = vim.client.factory.create('ns0:HostConfigSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'activeDirectory', 'datastorePrincipal', 'datastorePrincipalPasswd',
        'datetime', 'firewall', 'genericConfig', 'license', 'memory', 'nasDatastore',
        'network', 'nicTypeSelection', 'option', 'security', 'service',
        'storageDevice', 'userAccount', 'usergroupAccount', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    