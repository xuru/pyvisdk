
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HttpNfcLease(BaseEntity):
    '''A lease is in one of four states:
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HttpNfcLease):
        # MUST define these
        super(HttpNfcLease, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def error(self):
        '''If the lease is in the error state, this property contains the error that caused
        the lease to be aborted.
        '''
        return self.update('error')

    @property
    def info(self):
        '''Provides information on the objects contained in this lease. The info property is
        only valid when the lease is in the ready state.
        '''
        return self.update('info')

    @property
    def initializeProgress(self):
        '''Provides progress information (0-100 percent) for the initializing state of the
        lease. Clients can use this to track overall progress.
        '''
        return self.update('initializeProgress')

    @property
    def state(self):
        '''The current state of the lease.
        '''
        return self.update('state')


    def HttpNfcLeaseAbort(self, fault):
        '''Aborts the import/export and releases this lease. Operations on the objects
        contained in this lease will no longer be blocked. After calling this
        method, this lease will no longer be valid.Clients should call this method
        if an error occurs while accessing the disks, or if the operation is
        cancelled. The client can report the cause of the abort to other clients
        listening on the task with the fault parameter.

        :param fault: [in] The fault that caused the abort, if any.

        '''
        
        return self.delegate("HttpNfcLeaseAbort")(fault)
        

    def HttpNfcLeaseComplete(self):
        '''Completes the import/export and releases this lease. Operations on the objects
        contained in this lease will no longer be blocked. After calling this
        method, this lease will no longer be valid.Clients should call this method
        when they are done accessing the disks for the VirtualMachines in this
        lease. The status of the corresponding task will be set to success.
        '''
        
        return self.delegate("HttpNfcLeaseComplete")()
        

    def HttpNfcLeaseGetManifest(self):
        '''Gets the download manifest for this lease.

        :rtype: HttpNfcLeaseManifestEntry[] 

        '''
        
        return self.delegate("HttpNfcLeaseGetManifest")()
        

    def HttpNfcLeaseProgress(self, percent):
        '''Sets the disk up/download progress, and renews this lease. A lease will time out
        automatically after a while. If the client wishes to continue using it,
        for example if it is not done accessing the disks, this method must be
        called periodically.

        :param percent: [in] Completion status represented as an integer in the 0-100 range.

        '''
        
        return self.delegate("HttpNfcLeaseProgress")(percent)
        
