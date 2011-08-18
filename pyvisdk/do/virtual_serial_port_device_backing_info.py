# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualSerialPortDeviceBackingInfo(vim, *args, **kwargs):
    '''The data object defines information for using a host serial port device as
    backing for a . On a host, the first virtual machine to configure physical
    device backing for a virtual serial port will obtain the mapping. As long as
    that machine maintains the backing, any additional attempts to configure
    backing using that device will fail (a recoverable error, see the connection
    info ).'''
    
    obj = vim.client.factory.create('ns0:VirtualSerialPortDeviceBackingInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'deviceName', 'useAutoDetect' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    