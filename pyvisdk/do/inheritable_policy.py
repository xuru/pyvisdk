
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def InheritablePolicy(vim, *args, **kwargs):
    '''The base class for any type of setting or configuration that may get a
    inherited value.When used in a reconfgure operation specification, if inherited
    is true, it specifies the intention to change the values of subclass's
    properties to the inhertied values from the level above. In this case, users
    don't need to specify the values and any set property in the subclass will be
    ignored. if inherited is false, it specifies the intension to explicitly set
    subclass's properties to user specified values. Users should set the properties
    in the subclass with the desired values.When used in a configuration
    information object, The values of the properties in the subclass are the
    effective values. if inherited is true, the object is getting the effective
    values from upper level. If false, the values are explicitly set by a user.'''
    
    obj = vim.client.factory.create('ns0:InheritablePolicy')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'inherited' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    