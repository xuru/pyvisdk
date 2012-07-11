
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DiagnosticManager(BaseEntity):
    '''Provides an interface to get low-level debugging logs or diagnostic bundles for
    a server. For VirtualCenter, this includes the log files for the server daemon.
    For an ESX Server host, this includes detailed log files for the VMkernel.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.DiagnosticManager):
        super(DiagnosticManager, self).__init__(core, name=name, ref=ref, type=type)

    

    
    
    def BrowseDiagnosticLog(self, key, host=None, start=None, lines=None):
        '''Returns part of a log file. Log entries are always returned chronologically,
        typically with the newest event last.
        
        :param host: Specifies the host. If not specified, then it defaults to the default server. For example, if called on VirtualCenter, then the value defaults to VirtualCenter logs.
        
        :param key: A string key specifying the key for the log file to browse. Keys can be obtained using the queryDescriptions method.
        
        :param start: The line number for the first entry to be returned. If the parameter is not specified, then the operation returns with lines starting from the top of the log.
        
        :param lines: The number of lines to return. If not specified, then all lines are returned from the start value to the end of the file.
        
        '''
        return self.delegate("BrowseDiagnosticLog")(host, key, start, lines)
    
    def GenerateLogBundles_Task(self, includeDefault, host=None):
        '''Instructs the server to generate diagnostic bundles. A diagnostic bundle
        includes log files and other configuration information that can be used to
        investigate potential server issues. Virtual machine and guest operation system
        state is excluded from diagnostic bundles.
        
        :param includeDefault: Specifies if the bundle should include the default server. If called on a VirtualCenter server, then this means the VirtualCenter diagnostic files. If called directly on a host, then includeDefault must be set to true.
        
        :param host: Lists hosts that are included. This is only used when called on VirtualCenter. If called directly on a host, then this parameter must be empty.
        
        '''
        return self.delegate("GenerateLogBundles_Task")(includeDefault, host)
    
    def QueryDescriptions(self, host=None):
        '''Returns a list of diagnostic files for a given system.
        
        :param host: Specifies the host. If not specified, then it defaults to the server itself. For example, if called on VirtualCenter, then the value defaults to VirtualCenter logs. When called on an ESX server host, the host should not be specified.
        
        '''
        return self.delegate("QueryDescriptions")(host)