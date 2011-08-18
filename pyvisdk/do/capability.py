# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def Capability(vim, *args, **kwargs):
    '''A particular product may or may not support certain features. This data object
    indicates whether or not a service instance implements these features. This
    data object type indicates the circumstances under which an operation throws a
    NotSupported fault.Support for some features is indicated by the presence or
    absence of the manager object from the service instance. For example, the
    AlarmManager manager object indicates collecting alarms is supported. Other
    features indicate whether or not a given operation on an object throws a
    NotSupported fault.Some capabilities depend on the host or virtual machine
    version. These are specified by using the vim.host.Capability and
    vim.vm.Capability objects.'''
    
    obj = vim.client.factory.create('ns0:Capability')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'multiHostSupported', 'provisioningSupported', 'supportedEVCMode',
        'userShellAccessSupported' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    