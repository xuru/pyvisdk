
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmPortGroupProfile(vim, *args, **kwargs):
    '''The VmPortGroupProfile data object represents the subprofile for a port group
    that will be used by virtual machines. Use the policy list for access to
    configuration data for the virtual machine port group profile. Use the property
    list for access to subprofiles, if any.vSphere Servers use Network managed
    objects to represent virtual machine port groups in the vSphere inventory.'''
    
    obj = vim.client.factory.create('ns0:VmPortGroupProfile')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 7 arguments got: %d' % len(args))

    required = [ 'key', 'name', 'networkPolicy', 'vlan', 'vswitch', 'enabled' ]
    optional = [ 'policy', 'profileTypeName', 'profileVersion', 'property', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    