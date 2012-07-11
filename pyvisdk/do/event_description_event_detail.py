
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def EventDescriptionEventDetail(vim, *args, **kwargs):
    '''Each Event object provides an automatic event message string through its
    fullFormattedMessage property. However, you can use the EventDetail object's
    properties to format an event message string that is appropriate when viewed
    from a specific context. The variable information (vm.name, and so on) is
    derived from the Event object's event arguments (VmEventArgument, and so on).'''
    
    obj = vim.client.factory.create('ns0:EventDescriptionEventDetail')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 8 arguments got: %d' % len(args))

    required = [ 'category', 'formatOnComputeResource', 'formatOnDatacenter', 'formatOnHost',
        'formatOnVm', 'fullFormat', 'key' ]
    optional = [ 'description', 'longDescription', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    