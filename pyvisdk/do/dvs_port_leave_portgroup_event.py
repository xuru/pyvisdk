
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DvsPortLeavePortgroupEvent(vim, *args, **kwargs):
    '''A port was moved out of the distributed virtual portgroup.'''
    
    obj = vim.client.factory.create('ns0:DvsPortLeavePortgroupEvent')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 8 arguments got: %d' % len(args))
        
    signature = [ 'chainId', 'createdTime', 'key', 'userName', 'portgroupKey', 'portgroupName',
        'portKey' ]
    inherited = [ 'changeTag', 'computeResource', 'datacenter', 'ds', 'dvs',
        'fullFormattedMessage', 'host', 'net', 'vm' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    