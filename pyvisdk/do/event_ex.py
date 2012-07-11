
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def EventEx(vim, *args, **kwargs):
    '''EventEx is a dynamically typed Event class, whose type is indicated by its
    eventTypeId property.A collection of eventTypeIds is registered by Extensions,
    which can now pass in optional type information for each eventTypeId which
    indicates the applicable argument names and types, among other
    properties.EventEx allows event arguments of any type, though today, the system
    only supports "string" and "moid" (a string which can be interpreted as an
    object ID in the system) as argument types. In the future, the system may
    optionally strongly check the types of the arguments in the event against the
    declared type information, based on how the event type is declared.EventEx also
    allows arbitrary "event object"s - the object which the event refers to. You
    can put in any object identifier as the objectId, but objectType should be
    filled in only if the object is actually present in the VC Server's
    ManagedEntity inventory.'''
    
    obj = vim.client.factory.create('ns0:EventEx')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'eventTypeId', 'chainId', 'createdTime', 'key', 'userName' ]
    optional = [ 'arguments', 'fault', 'message', 'objectId', 'objectName', 'objectType',
        'severity', 'changeTag', 'computeResource', 'datacenter', 'ds', 'dvs',
        'fullFormattedMessage', 'host', 'net', 'vm', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    