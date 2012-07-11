
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class GuestProcessManager(BaseEntity):
    '''ProcessManager is the managed object that provides APIs to manipulate the guest
    operating system processes.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.GuestProcessManager):
        super(GuestProcessManager, self).__init__(core, name=name, ref=ref, type=type)

    

    
    
    def ListProcessesInGuest(self, vm, auth, pids=None):
        '''List the processes running in the guest operating system, plus those started by
        StartProgramInGuest that have recently completed.
        
        :param vm: Virtual machine to perform the operation on.
        
        :param auth: The guest authentication data. See GuestAuthentication.
        
        :param pids: If set, only return information about the specified processes. Otherwise, information about all processes are returned. If a specified processes does not exist, nothing will be returned for that process.
        
        '''
        return self.delegate("ListProcessesInGuest")(vm, auth, pids)
    
    def ReadEnvironmentVariableInGuest(self, vm, auth, names=None):
        '''Reads an environment variable from the guest OSReads an environment variable
        from the guest OS
        
        :param vm: Virtual machine to perform the operation on.
        
        :param auth: The guest authentication data. See GuestAuthentication.
        
        :param names: The names of the variables to be read. If not set, then all the environment variables are returned.
        
        '''
        return self.delegate("ReadEnvironmentVariableInGuest")(vm, auth, names)
    
    def StartProgramInGuest(self, vm, auth, spec):
        '''Starts a program in the guest operating system.Starts a program in the guest
        operating system.
        
        :param vm: Virtual machine to perform the operation on.
        
        :param auth: The guest authentication data. See GuestAuthentication.
        
        :param spec: The arguments describing the program to be started.
        
        '''
        return self.delegate("StartProgramInGuest")(vm, auth, spec)
    
    def TerminateProcessInGuest(self, vm, auth, pid):
        '''Terminates a process in the guest OS.
        
        :param vm: Virtual machine to perform the operation on.
        
        :param auth: The guest authentication data. See GuestAuthentication.
        
        :param pid: Process ID of the process to be terminated
        
        '''
        return self.delegate("TerminateProcessInGuest")(vm, auth, pid)