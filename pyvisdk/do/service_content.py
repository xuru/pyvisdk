
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ServiceContent(vim, *args, **kwargs):
    ''''''
    
    obj = vim.client.factory.create('ns0:ServiceContent')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))
        
    signature = [ 'about', 'propertyCollector', 'rootFolder' ]
    inherited = [ 'accountManager', 'alarmManager', 'authorizationManager',
        'clusterProfileManager', 'complianceManager', 'customFieldsManager',
        'customizationSpecManager', 'diagnosticManager', 'dvSwitchManager',
        'eventManager', 'extensionManager', 'fileManager', 'hostProfileManager',
        'ipPoolManager', 'licenseManager', 'localizationManager', 'ovfManager',
        'perfManager', 'scheduledTaskManager', 'searchIndex', 'sessionManager',
        'setting', 'snmpSystem', 'storageResourceManager', 'taskManager',
        'userDirectory', 'viewManager', 'virtualDiskManager', 'virtualizationManager',
        'vmCompatibilityChecker', 'vmProvisioningChecker' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    