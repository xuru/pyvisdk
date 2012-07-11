
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationGuiRunOnce(vim, *args, **kwargs):
    '''The commands listed in the GuiRunOnce data object type are executed when a user
    logs on the first time after customization completes. The logon may be driven
    by the AutoLogon setting.The GuiRunOnce data object type maps to the GuiRunOnce
    key in the answer file. These values are transferred into the file that
    VirtualCenter stores on the target virtual disk. For more detailed information,
    see the document .'''
    
    obj = vim.client.factory.create('ns0:CustomizationGuiRunOnce')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'commandList' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    