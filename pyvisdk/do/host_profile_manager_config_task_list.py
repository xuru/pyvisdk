
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostProfileManagerConfigTaskList(vim, *args, **kwargs):
    '''The HostProfileManagerConfigTaskList data object represents a set of tasks to
    be performed on a host during host profile application.'''
    
    obj = vim.client.factory.create('ns0:HostProfileManagerConfigTaskList')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'configSpec', 'taskDescription', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    