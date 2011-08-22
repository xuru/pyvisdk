
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
        
    signature = [ 'enabled', 'key', 'label', 'required', 'rule' ]
    inherited = [ 'service' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    