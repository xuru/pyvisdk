
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
    
    

    def BrowseDiagnosticLog(self, key):
        '''Returns part of a log file. Log entries are always returned chronologically,
        typically with the newest event last.

        :param key: A string key specifying the key for the log file to browse. Keys can be obtained using the queryDescriptions method.


        :rtype: DiagnosticManagerLogHeader 

        '''
        
        return self.delegate("BrowseDiagnosticLog")(key)
        

    def QueryDescriptions(self):
        '''Returns a list of diagnostic files for a given system.

        :rtype: DiagnosticManagerLogDescriptor[] 

        '''
        
        return self.delegate("QueryDescriptions")()
        

    def GenerateLogBundles_Task(self, includeDefault):
        '''Instructs the server to generate diagnostic bundles. A diagnostic bundle includes
        log files and other configuration information that can be used to
        investigate potential server issues. Virtual machine and guest operation
        system state is excluded from diagnostic bundles.

        :param includeDefault: Specifies if the bundle should include the default server. If called on a VirtualCenter server, then this means the VirtualCenter diagnostic files. If called directly on a host, then includeDefault must be set to true.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("GenerateLogBundles_Task")(includeDefault)
        
