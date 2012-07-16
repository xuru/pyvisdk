
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationSpec(vim, *args, **kwargs):
    '''The Specification data object type contains information required to customize a
    virtual machine when deploying it or migrating it to a new host.'''
    
    obj = vim.client.factory.create('ns0:CustomizationSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'globalIPSettings', 'identity' ]
    optional = [ 'encryptionKey', 'nicSettingMap', 'options', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    