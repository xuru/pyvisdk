# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterRuleInfo(vim, *args, **kwargs):
    '''The ClusterRuleInfo data object is the base type for affinity and anti-affinity
    rules. The affinity and anti-affinity rules are DRS (Distributed Resource
    Scheduling) rules that affect the placement of virtual machines in a cluster.
    Hosts and virtual machines referenced in a DRS rule must be in the same
    cluster.Note: DRS rules are different than an individual host's CPU affinity
    rules (VirtualMachineAffinityInfo).The Server uses DRS rule objects to describe
    the current rule configuration (ClusterConfigInfoEx.rule). Your client
    application uses rule objects to configure the affinity and anti-affinity rules
    (ClusterConfigSpecEx.rulesSpec).You can create the following types of
    rules:Rule configuration is a dynamic process. When you create or modify a DRS
    rule, the Server applies the rule to the cluster. If the existing cluster
    configuration violates the rule, the Server attempts to correct the situation.
    If that is not possible, the Server generates a fault and produces a log event.
    DRS rules do not have precedence; all rules are applied equally. DRS does not
    validate one rule against another. If you create conflicting rules, the older
    rule takes precedence and DRS disables the newer rule.Improperly used, DRS
    rules can fragment the cluster and inhibit the proper functioning of DRS, HA,
    and DPM services. vSphere services never take any actions that would result in
    the violation of mandatory DRS rules. An operation that violates a mandatory
    rule would produce the following consequences.To avoid these situations,
    exercise caution when creating more than one mandatory rule, or consider using
    only optional rules. Make sure that the number of hosts with which a virtual
    machine is related by affinity rule is large enough that losing a host does not
    prevent the virtual machine from running.For manual and partially automated DRS
    clusters, the Server produces migration recommendations to satisfy the DRS
    rules. You are not required to act on the recommendations, but the Server
    maintains the recommendations until the rules are satisfied.'''
    
    obj = vim.client.factory.create('ns0:ClusterRuleInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'enabled', 'inCompliance', 'key', 'mandatory', 'name', 'status', 'userCreated' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    