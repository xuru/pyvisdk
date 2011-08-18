# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AuthorizationPrivilege(vim, *args, **kwargs):
    '''This data object type provides access to some aspect of the system. Privileges
    are generally independent. This means a user with a privilege usually can
    perform an associated set of actions without needing any additional supporting
    privileges.Within each product version, privileges do not change. See
    AuthorizationDescription for detailed information on the privileges defined by
    the system.'''
    
    obj = vim.client.factory.create('ns0:AuthorizationPrivilege')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'name', 'onParent', 'privGroupName', 'privId' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    