
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualSwitchProfile(vim, *args, **kwargs):
    '''The VirtualSwitchProfile data object represents a subprofile for a virtual
    switch. If a profile plug-in defines policies or subprofiles, use the policy or
    property list to access the additional configuration data.'''
    
    obj = vim.client.factory.create('ns0:VirtualSwitchProfile')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 7 arguments got: %d' % len(args))

    required = [ 'key', 'link', 'name', 'networkPolicy', 'numPorts', 'enabled' ]
    optional = [ 'policy', 'profileTypeName', 'profileVersion', 'property', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    