
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DiagnosticManager(BaseEntity):
    '''Provides an interface to get low-level debugging logs or diagnostic bundles for a
        server. For VirtualCenter, this includes the log files for the server
        daemon. For an ESX Server host, this includes detailed log files for the
        VMkernel.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.DiagnosticManager):
        # MUST define these
        super(DiagnosticManager, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def BrowseDiagnosticLog(self, host):
        '''Returns part of a log file. Log entries are always returned chronologically,
        typically with the newest event last.

        :param host: to a HostSystemSpecifies the host. If not specified, then it defaults to the
        server itself. For example, if called on VirtualCenter, then the value
        defaults to VirtualCenter logs. When called on an ESX server host, the
        host should not be specified.


        :rtype: DiagnosticManagerLogDescriptor[] 

        '''
        
        return self.delegate("BrowseDiagnosticLog")(host)
        

    def GenerateLogBundles_Task(self, host):
        '''Instructs the server to generate diagnostic bundles. A diagnostic bundle includes
        log files and other configuration information that can be used to
        investigate potential server issues. Virtual machine and guest operation
        system state is excluded from diagnostic bundles.

        :param host: to a HostSystemSpecifies the host. If not specified, then it defaults to the
        server itself. For example, if called on VirtualCenter, then the value
        defaults to VirtualCenter logs. When called on an ESX server host, the
        host should not be specified.


        :rtype: DiagnosticManagerLogDescriptor[] 

        '''
        
        return self.delegate("GenerateLogBundles_Task")(host)
        

    def QueryDescriptions(self, host):
        '''Returns a list of diagnostic files for a given system.

        :param host: to a HostSystemSpecifies the host. If not specified, then it defaults to the
        server itself. For example, if called on VirtualCenter, then the value
        defaults to VirtualCenter logs. When called on an ESX server host, the
        host should not be specified.


        :rtype: DiagnosticManagerLogDescriptor[] 

        '''
        
        return self.delegate("QueryDescriptions")(host)
        
