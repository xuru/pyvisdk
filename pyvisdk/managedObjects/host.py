'''
Created on Mar 8, 2011

@author: eplaster
'''
from pyvisdk.consts import ManagedEntityTypes
from pyvisdk.managedObjects.managedentity import ManagedEntity
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

class HostSystem(ManagedEntity):
    def __init__(self, core, name=None, ref=None):
        # MUST define these
        self.type = ManagedEntityTypes.HostSystem # IGNORE E1101
        props = [ "capability", "config", "configManager", "datastore", "datastoreBrowser", "hardware", 
                 "network", "runtime", "summary", "systemResources", "vm"]
        
        methods = ["AcquireCimServicesTicket", "DisconnectHost_Task", "EnterLockdownMode", 
            "EnterMaintenanceMode_Task", "ExitLockdownMode", "ExitMaintenanceMode_Task", "PowerDownHostToStandBy_Task", 
            "PowerUpHostFromStandBy_Task", "QueryHostConnectionInfo", "QueryMemoryOverhead", "QueryMemoryOverheadEx", 
            "RebootHost_Task", "ReconfigureHostForDAS_Task", "ReconnectHost_Task", "RetrieveHardwareUptime", 
            "ShutdownHost_Task", "UpdateFlags", "UpdateIpmi", "UpdateSystemResources"]
                            
        super(HostSystem, self).__init__(core, methods, props, name, ref)
        
