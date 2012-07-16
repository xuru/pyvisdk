
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def OptionDef(vim, *args, **kwargs):
    '''Describes a user-defined option. The name of each option is identified by the
    "key" property, inherited from the ElementDescription data object type. You can
    indicate the property's position in a hierarchy by using a dot-separated
    notation. The string preceding the first dot is the top of the hierarchy. The
    hierarchy descends to a new sublevel with each dot. For example,
    "Ethernet.NetworkConnection.Bridged".'''
    
    obj = vim.client.factory.create('ns0:OptionDef')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'optionType', 'key', 'label', 'summary' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    