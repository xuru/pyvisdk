
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPatchManager(BaseEntity):
    '''This managed object is the interface for scanning and patching an ESX server.
        VMware publishes updates through its external website. A patch update is
        synonymous with a bulletin. An update may contain many individual patch
        binaries, but its installation and uninstallation are atomic.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostPatchManager):
        # MUST define these
        super(HostPatchManager, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def CheckHostPatch_Task(self, bulletinIds):
        '''Check the list of metadata and returns the dependency, obsolete and conflict
        information The operation is cancelable through the returned Task object.
        No integrity checks are performed on the metadata.

        :param bulletinIds: A list of bulletin IDs to be removed.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CheckHostPatch_Task")(bulletinIds)
        

    def InstallHostPatch_Task(self, bulletinIds):
        '''Deprecated. Method is deprecated, use InstallHostPatchV2_Task instead. Patch the
        host. The operation is not cancelable. If the patch installation failed,
        an atomic rollback of the installation will be attempted. Manual rollback
        is required if the atomic rollback failed, see PatchInstallFailed for
        details.

        :param bulletinIds: A list of bulletin IDs to be removed.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("InstallHostPatch_Task")(bulletinIds)
        

    def InstallHostPatchV2_Task(self, bulletinIds):
        '''Patch the host. The operation is not cancelable. If the patch installation failed,
        an atomic rollback of the installation will be attempted. Manual rollback
        is required if the atomic rollback failed, see PatchInstallFailed for
        details.

        :param bulletinIds: A list of bulletin IDs to be removed.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("InstallHostPatchV2_Task")(bulletinIds)
        

    def QueryHostPatch_Task(self, bulletinIds):
        '''Query the host for installed bulletins.

        :param bulletinIds: A list of bulletin IDs to be removed.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("QueryHostPatch_Task")(bulletinIds)
        

    def ScanHostPatch_Task(self, bulletinIds):
        '''Deprecated. As of VI API 4.0, use ScanHostPatchV2_Task. Scan the host for the
        patch status. The operation is cancelable through the returned Task
        object. Integrity checks are performed on the metadata only during the
        scan operation.

        :param bulletinIds: A list of bulletin IDs to be removed.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("ScanHostPatch_Task")(bulletinIds)
        

    def ScanHostPatchV2_Task(self, bulletinIds):
        '''Scan the host for the patch status. The operation is cancelable through the
        returned Task object. Integrity checks are performed on the metadata only
        during the scan operation.

        :param bulletinIds: A list of bulletin IDs to be removed.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("ScanHostPatchV2_Task")(bulletinIds)
        

    def StageHostPatch_Task(self, bulletinIds):
        '''Stage the vib files to esx local location and possibly do some run time check.

        :param bulletinIds: A list of bulletin IDs to be removed.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("StageHostPatch_Task")(bulletinIds)
        

    def UninstallHostPatch_Task(self, bulletinIds):
        '''Uninstall patch from the host. The operation is not cancelable.

        :param bulletinIds: A list of bulletin IDs to be removed.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("UninstallHostPatch_Task")(bulletinIds)
        
