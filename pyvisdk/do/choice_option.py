
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ChoiceOption(vim, *args, **kwargs):
    '''The ChoiceOption data object type defines a set of supported string values, a
    localizable description for each value, and the default value.'''
    
    obj = vim.client.factory.create('ns0:ChoiceOption')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'choiceInfo' ]
    optional = [ 'defaultIndex', 'valueIsReadonly', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    