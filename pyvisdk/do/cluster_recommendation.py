
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
        
    signature = [ 'key', 'rating', 'reason', 'reasonText', 'time', 'type' ]
    inherited = [ 'action', 'prerequisite', 'target' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    