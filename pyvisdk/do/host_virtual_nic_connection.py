# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostVirtualNicConnection(vim, *args, **kwargs):
    '''DataObject which provides a level of indirection when identifying VirtualNics
    during configuration. This dataObject lets users specify a VirtualNic in terms
    of the portgroup/Dv Port the vnic is connected to. This is useful in cases
    where VirtualNic will be created as part of a configuration operation and the
    created VirtualNic is referred to in some other part of configuration. e.g: for
    configuring VMotion'''
    
    obj = vim.client.factory.create('ns0:HostVirtualNicConnection')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'dvPort', 'portgroup' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    