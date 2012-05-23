
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostFirewallRuleset(vim, *args, **kwargs):
    '''Data object that describes a single network ruleset that can be allowed or
    blocked by the firewall using the HostFirewallSystem object.'''
    
    obj = vim.client.factory.create('ns0:HostFirewallRuleset')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'enabled', 'key', 'label', 'required', 'rule' ]
    optional = [ 'allowedHosts', 'service', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    