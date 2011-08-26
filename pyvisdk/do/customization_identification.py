
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationIdentification(vim, *args, **kwargs):
    '''The Identification data object type maps to the Identification key in the
    answer file. These values are transferred into the file that VirtualCenter
    stores on the target virtual disk. For more detailed information, see the
    document .'''
    
    obj = vim.client.factory.create('ns0:CustomizationIdentification')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'domainAdmin', 'domainAdminPassword', 'joinDomain', 'joinWorkgroup' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    