
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
    
    
    
    
    
    def BrowseDiagnosticLog(self):
        '''Returns part of a log file. Log entries are always returned chronologically,
        typically with the newest event last.
        :rtype: 
        :returns: 
        '''
        return self.delegate("BrowseDiagnosticLog")()
    
    def GenerateLogBundles_Task(self):
        '''Instructs the server to generate diagnostic bundles. A diagnostic bundle
        includes log files and other configuration information that can be used to
        investigate potential server issues. Virtual machine and guest operation system
        state is excluded from diagnostic bundles.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("GenerateLogBundles_Task")()
    
    def QueryDescriptions(self):
        '''Returns a list of diagnostic files for a given system.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryDescriptions")()