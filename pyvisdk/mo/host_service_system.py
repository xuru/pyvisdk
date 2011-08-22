
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostServiceSystem(ExtensibleManagedObject):
    '''The ServiceSystem managed object describes the configuration of host services.
    This managed object operates in conjunction with the HostFirewallSystem managed
    object.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostServiceSystem):
        super(HostServiceSystem, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def serviceInfo(self):
        '''Service configuration.'''
        return self.update('serviceInfo')
    
    
    
    def RefreshServices(self):
        '''Refresh the service information and settings to pick up any changes made
        directly on the host.
        :rtype: None
        :returns: 
        '''
        return self.delegate("RefreshServices")()
    
    def RestartService(self):
        '''Restarts the service.
        :rtype: None
        :returns: 
        '''
        return self.delegate("RestartService")()
    
    def StartService(self):
        '''Starts the service.
        :rtype: None
        :returns: 
        '''
        return self.delegate("StartService")()
    
    def StopService(self):
        '''Stops the service.
        :rtype: None
        :returns: 
        '''
        return self.delegate("StopService")()
    
    def UninstallService(self):
        '''Uninstalls the service. If the service is running, it is stopped before being
        uninstalled.
        :rtype: None
        :returns: 
        '''
        return self.delegate("UninstallService")()
    
    def UpdateServicePolicy(self):
        '''Updates the activation policy (HostServicePolicy) of the service.
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdateServicePolicy")()