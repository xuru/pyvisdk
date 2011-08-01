
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
    
    

    def InstallHostPatchV2_Task(self):
        '''Patch the host. The operation is not cancelable. If the patch installation failed,
        an atomic rollback of the installation will be attempted. Manual rollback
        is required if the atomic rollback failed, see PatchInstallFailed for
        details.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("InstallHostPatchV2_Task")()
        

    def InstallHostPatch_Task(self, updateID, repository):
        '''Deprecated. Method is deprecated, use InstallHostPatchV2_Task instead. Patch the
        host. The operation is not cancelable. If the patch installation failed,
        an atomic rollback of the installation will be attempted. Manual rollback
        is required if the atomic rollback failed, see PatchInstallFailed for
        details.

        :param updateID: The update to be installed on the host.

        :param repository: Location of the repository that contains the bulletin depot. The depot must be organized as a flat collection of bulletins with each one being a folder named after the bulletin ID. Each folder must contain both update metadata and required binaries.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("InstallHostPatch_Task")(updateID,repository)
        

    def ScanHostPatch_Task(self, repository):
        '''Deprecated. As of VI API 4.0, use ScanHostPatchV2_Task. Scan the host for the
        patch status. The operation is cancelable through the returned Task
        object. Integrity checks are performed on the metadata only during the
        scan operation.

        :param repository: Location of the repository that contains the bulletin depot. The depot must be organized as a flat collection of bulletins with each one being a folder named after the bulletin ID. Each folder must contain the full update metadata.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("ScanHostPatch_Task")(repository)
        

    def StageHostPatch_Task(self):
        '''Stage the vib files to esx local location and possibly do some run time check.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("StageHostPatch_Task")()
        

    def UninstallHostPatch_Task(self):
        '''Uninstall patch from the host. The operation is not cancelable.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("UninstallHostPatch_Task")()
        

    def CheckHostPatch_Task(self):
        '''Check the list of metadata and returns the dependency, obsolete and conflict
        information The operation is cancelable through the returned Task object.
        No integrity checks are performed on the metadata.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CheckHostPatch_Task")()
        

    def QueryHostPatch_Task(self):
        '''Query the host for installed bulletins.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("QueryHostPatch_Task")()
        

    def ScanHostPatchV2_Task(self):
        '''Scan the host for the patch status. The operation is cancelable through the
        returned Task object. Integrity checks are performed on the metadata only
        during the scan operation.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("ScanHostPatchV2_Task")()
        
