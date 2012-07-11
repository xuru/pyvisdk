
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationUserData(vim, *args, **kwargs):
    '''Personal data pertaining to the owner of the virtual machine.The UserData data
    object type maps to the UserData key in the answer file. These values are
    transferred directly into the file that VirtualCenter stores on the target
    virtual disk. For more detailed information, see the document .'''
    
    obj = vim.client.factory.create('ns0:CustomizationUserData')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'computerName', 'fullName', 'orgName', 'productId' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    