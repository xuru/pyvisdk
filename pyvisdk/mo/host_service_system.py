
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.extensible_managed_object import ExtensibleManagedObject
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostServiceSystem(ExtensibleManagedObject):
    '''The ServiceSystem managed object describes the configuration of host services.
        This managed object operates in conjunction with the HostFirewallSystem
        managed object.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostServiceSystem):
        # MUST define these
        super(HostServiceSystem, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def serviceInfo(self):
        '''
        Service configuration.
        '''
        return self.update('serviceInfo')


    def RefreshServices(self):
        '''Refresh the service information and settings to pick up any changes made directly
        on the host.
        '''
        
        return self.delegate("RefreshServices")()
        

    def UninstallService(self, id):
        '''Uninstalls the service. If the service is running, it is stopped before being
        uninstalled.

        :param id: 

        '''
        
        return self.delegate("UninstallService")(id)
        

    def StopService(self, id):
        '''Stops the service.

        :param id: 

        '''
        
        return self.delegate("StopService")(id)
        

    def RestartService(self, id):
        '''Restarts the service.

        :param id: 

        '''
        
        return self.delegate("RestartService")(id)
        

    def StartService(self, id):
        '''Starts the service.

        :param id: 

        '''
        
        return self.delegate("StartService")(id)
        

    def UpdateServicePolicy(self, policy, id):
        '''Updates the activation policy (HostServicePolicy) of the service.

        :param policy: 

        :param id: 

        '''
        
        return self.delegate("UpdateServicePolicy")(policy,id)
        
