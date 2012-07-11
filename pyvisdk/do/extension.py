
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def Extension(vim, *args, **kwargs):
    '''This data object type contains all information about an extension. An extension
    may contain zero or more server interfaces and zero or more clients.'''
    
    obj = vim.client.factory.create('ns0:Extension')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'description', 'key', 'lastHeartbeatTime', 'version' ]
    optional = [ 'client', 'company', 'eventList', 'extendedProductInfo', 'faultList',
        'healthInfo', 'managedEntityInfo', 'ovfConsumerInfo', 'privilegeList',
        'resourceList', 'server', 'shownInSolutionManager', 'solutionManagerInfo',
        'subjectName', 'taskList', 'type', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    