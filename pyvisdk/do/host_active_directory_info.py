# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostActiveDirectoryInfo(vim, *args, **kwargs):
    '''The HostActiveDirectoryInfo data object describes ESX host membership in an
    Active Directory domain. If the HostAuthenticationStoreInfo.enabled property is
    , the host is a member of a domain and the ESX Server will set the domain
    information properties.'''
    
    obj = vim.client.factory.create('ns0:HostActiveDirectoryInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'enabled', 'domainMembershipStatus', 'joinedDomain', 'trustedDomain' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    