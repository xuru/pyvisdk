
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ProfileDeferredPolicyOptionParameter(vim, *args, **kwargs):
    '''The ProfileDeferredPolicyOptionParameter data object contains information about
    a single deferred parameter for host configuration.* The Server verifies
    deferred parameter data when it calls the HostProfile.ExecuteHostProfile
    method. * The client supplies deferred parameter data for host configuration
    when it calls the HostProfileManager.ApplyHostConfig_Task method. * The vCenter
    Server stores deferred parameter data in answer files (AnswerFile.userInput).'''
    
    obj = vim.client.factory.create('ns0:ProfileDeferredPolicyOptionParameter')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'inputPath' ]
    optional = [ 'parameter', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    