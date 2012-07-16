
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationLicenseFilePrintData(vim, *args, **kwargs):
    '''The LicenseFilePrintData type maps directly to the LicenseFilePrintData key in
    the answer file. These values are transferred into the file that VirtualCenter
    stores on the target virtual disk. For more detailed information, see the
    document . LicenseFilePrintData provides licensing information for Windows
    server operating systems.'''
    
    obj = vim.client.factory.create('ns0:CustomizationLicenseFilePrintData')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'autoMode' ]
    optional = [ 'autoUsers', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    