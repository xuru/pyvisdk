
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterRecommendation(vim, *args, **kwargs):
    '''Recommendation is the base class for any packaged group of actions that are
    intended to take the system from one state to another one.'''
    
    obj = vim.client.factory.create('ns0:ClusterRecommendation')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 7 arguments got: %d' % len(args))

    required = [ 'key', 'rating', 'reason', 'reasonText', 'time', 'type' ]
    optional = [ 'action', 'prerequisite', 'target', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    