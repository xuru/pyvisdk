# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostCpuIdInfo(vim, *args, **kwargs):
    '''The CpuIdInfo data object type is used to represent the CPU features of a
    particular host or product, or to specify what the CPU feature requirements are
    for a particular virtual machine or guest operating system.For each register
    (eax,ebx,ecx,edx), the string is a bit mask of the form:When used to represent
    the features of a specific processor package (cpuPkg), the features common to
    all processors on a host (cpuFeature), or the features supported by a
    virtualization platform (supportedCpuFeature), each bit is either '0' or '1',
    or '-' for unknown/unspecified. In these feature vectors, the vendor field is
    never set.Optional values in these feature vectors default to
    '----:----:----:----:----:----:----:----'.When specifying the required feature
    set for a virtual machine or a guest operating system, the bits can take on the
    values as described below, and the vendor field may be set. The total feature
    requirements for a virtual machine are composed by using any requirements
    listed in the virtual machine's configuration to override the requirements
    listed in the descriptor for the virtual machine's guest OS.Bits used for
    specifying requirements:The values 'F' and '1' are rarely used but included for
    completeness. The '0' and '1' values do not promise a faithful virtualization
    of these features; whether the features work when forced to 0 or 1 is highly
    dependent on the guest software.Optional values in the requirements from the
    virtual machine's configuration default to
    '----:----:----:----:----:----:----:----'. Optional values in the requirements
    from the guest OS descriptor default to
    'xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx'.Once the feature requirements for a
    virtual machine have been composed from the virtual machine's configuration and
    guest OS descriptor, the bit types above are used to identify whether or not
    the virtual machine can be powered on or be migrated with VMotion to a
    particular host. The rules are as follows:'''
    
    obj = vim.client.factory.create('ns0:HostCpuIdInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'eax', 'ebx', 'ecx', 'edx', 'level', 'vendor' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    