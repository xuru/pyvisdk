
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def UserInputRequiredParameterMetadata(vim, *args, **kwargs):
    '''The UserInputRequiredParameterMetadata data object represents policy option
    metadata information for configuration data. The Profile Engine saves
    configuration data from the user input options in the host AnswerFile. See the
    ExecuteHostProfile and ApplyHostConfig_Task methods.'''
    
    obj = vim.client.factory.create('ns0:UserInputRequiredParameterMetadata')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'id' ]
    optional = [ 'userInputParameter', 'parameter', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    