
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PerfInterval(vim, *args, **kwargs):
    '''This data object type contains metadata about a performance interval.* For
    VirtualCenter Server systems, instances of this data object are referred to as
    historical intervals because they control how data collected from the ESX
    systems will be aggregated and stored in the database. * For ESX system, this
    data object is typically referred to simply as the interval or performance
    interval because ESX does not aggregate statistical data.For ESX systems, a
    single instance of this data object exists. It cannot be modified. It has these
    properties:VirtualCenter Server system provides four instances of this data
    object by default, that apply globally to all system entities.VirtualCenter
    Server uses the specifications configured in its historical intervals to
    collect metrics from the ESX systems that it manages. The quantity of data
    collected depends on the level settings for the server, and the level
    associated with a specific counter. Both factors may change from one version of
    the products to the next. In general, the lower the number, the smaller the
    amount of data collected. For VirtualCenter Server 2.5, for example, the levels
    1 through 4 collected data as follows:Default properties for the four built-in
    historical intervals include:All values are in seconds. The default setting for
    vCenter Server is level 1, which retains sampled statistical data as follows:*
    5-minute samples for the past day * 30-minute samples for the past week *
    2-hour samples for the past month * 1-day samples for the past yearData older
    than a year is purged from the vCenter Server database.Prior to version 2.5 of
    the API, this data object could be used in conjunction with the
    CreatePerfInterval operation, to define new, custom historical intervals. That
    operation has been deprecated: Adding and deleting objects of this type is no
    longer supported. However, the default historical intervals can be enabled or
    disabled, and can be modified within certain limits (with the
    UpdatePerfInterval operation).'''
    
    obj = vim.client.factory.create('ns0:PerfInterval')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'enabled', 'key', 'length', 'name', 'samplingPeriod' ]
    optional = [ 'level', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    