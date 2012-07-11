
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def OvfConsumerOstNode(vim, *args, **kwargs):
    '''A node in the OVF section tree.This class represents a node on which OVF
    sections can be defined. The possible node types are OstNodeType.envelope,
    OstNodeType.virtualSystem or OstNodeType.virtualSystemCollection, corresponding
    to the identically named OVF element types.Since the node contains a list of
    children, it can also be regarded as a tree. This tree mirrors the structure of
    the OVF descriptor. It is provided to OVF consumers as a more convenient way to
    navigate and modify the OVF than by working directly on the XML.'''
    
    obj = vim.client.factory.create('ns0:OvfConsumerOstNode')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'id', 'type' ]
    optional = [ 'child', 'entity', 'section', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    