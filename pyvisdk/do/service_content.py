
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ServiceContent(vim, *args, **kwargs):
    '''The ServiceContent data object defines properties for the ServiceInstance
    managed object. The ServiceInstance itself does not have directly-accessible
    properties because reading the properties of a managed object requires the use
    of a property collector, and the property collector itself is a property of the
    ServiceInstance. For this reason, use the method RetrieveServiceContent to
    retrieve the ServiceContent object.'''
    
    obj = vim.client.factory.create('ns0:ServiceContent')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'about', 'propertyCollector', 'rootFolder' ]
    optional = [ 'accountManager', 'alarmManager', 'authorizationManager',
        'clusterProfileManager', 'complianceManager', 'customFieldsManager',
        'customizationSpecManager', 'diagnosticManager', 'dvSwitchManager',
        'eventManager', 'extensionManager', 'fileManager', 'guestOperationsManager',
        'hostProfileManager', 'ipPoolManager', 'licenseManager', 'localizationManager',
        'ovfManager', 'perfManager', 'scheduledTaskManager', 'searchIndex',
        'sessionManager', 'setting', 'snmpSystem', 'storageResourceManager',
        'taskManager', 'userDirectory', 'viewManager', 'virtualDiskManager',
        'virtualizationManager', 'vmCompatibilityChecker', 'vmProvisioningChecker',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    