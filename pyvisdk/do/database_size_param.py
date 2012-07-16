
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DatabaseSizeParam(vim, *args, **kwargs):
    '''DatabaseSizeParam contains information about a sample inventory. Using this
    information, database size requirements for that sample inventory can be
    computed. Depending on the accuracy of estimate desired, users can choose to
    specify the number of different types of managed entities. The numHosts and
    numVirtualMachines are the only two required fields. Rest are all optional
    fields filled up by Virtual Center based on some heuristics. These parameters
    need not represent a real inventory. The user can use these parameters to
    estimate the database size required by a hypothetical VirtualCenter setup.'''
    
    obj = vim.client.factory.create('ns0:DatabaseSizeParam')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'inventoryDesc' ]
    optional = [ 'perfStatsDesc', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    