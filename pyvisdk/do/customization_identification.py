
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationIdentification(vim, *args, **kwargs):
    '''The Identification data object type provides information needed to join a
    workgroup or domain.The Identification data object type maps to the
    Identification key in the answer file. These values are transferred into the
    file that VirtualCenter stores on the target virtual disk. For more detailed
    information, see the document .'''
    
    obj = vim.client.factory.create('ns0:CustomizationIdentification')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'domainAdmin', 'domainAdminPassword', 'joinDomain', 'joinWorkgroup',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    