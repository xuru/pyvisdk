
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostProfileConfigInfo(vim, *args, **kwargs):
    '''The HostProfileConfigInfo data object contains host profile data and
    information about profile compliance.'''
    
    obj = vim.client.factory.create('ns0:HostProfileConfigInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'enabled', 'name' ]
    optional = [ 'applyProfile', 'customComplyProfile', 'defaultComplyLocator',
        'defaultComplyProfile', 'disabledExpressionList', 'annotation',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    