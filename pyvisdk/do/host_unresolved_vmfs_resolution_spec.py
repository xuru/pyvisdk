# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostUnresolvedVmfsResolutionSpec(vim, *args, **kwargs):
    '''An unresolved VMFS volume is reported when one or more device partitions of
    volume are detected to have copies of extents of the volume. Such copies can be
    created via replication or snapshots, for example. This data object type
    describes how to resolve an unbound VMFS volume. The SCSI device path for each
    of the VMFS volume extent should be specified. For the current release, only
    head-extent needs to be specified. In future releases, we will allow user to
    specify explicitly all the extents which makes up a new Vmfs Volume.'''
    
    obj = vim.client.factory.create('ns0:HostUnresolvedVmfsResolutionSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'extentDevicePath', 'uuidResolution' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    