
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPatchManager(BaseEntity):
    '''This managed object is the interface for scanning and patching an ESX server.
    VMware publishes updates through its external website. A patch update is
    synonymous with a bulletin. An update may contain many individual patch
    binaries, but its installation and uninstallation are atomic.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostPatchManager):
        super(HostPatchManager, self).__init__(core, name=name, ref=ref, type=type)

    

    
    
    def CheckHostPatch_Task(self, metaUrls=None, bundleUrls=None, spec=None):
        '''Check the list of metadata and returns the dependency, obsolete and conflict
        information The operation is cancelable through the returned Task object. No
        integrity checks are performed on the metadata.
        
        :param metaUrls: a list of urls pointing to metadata.zip.
        
        :param bundleUrls: a list of urls pointing to an "offline" bundle.
        
        :param spec: 
        
        '''
        return self.delegate("CheckHostPatch_Task")(metaUrls, bundleUrls, spec)
    
    def InstallHostPatch_Task(self, repository, updateID, force=None):
        '''<b>Deprecated.</b> <i>Method is deprecated, use InstallHostPatchV2_Task
        instead.</i> Patch the host. The operation is not cancelable. If the patch
        installation failed, an atomic rollback of the installation will be attempted.
        Manual rollback is required if the atomic rollback failed, see
        PatchInstallFailed for details.
        
        :param repository: Location of the repository that contains the bulletin depot. The depot must be organized as a flat collection of bulletins with each one being a folder named after the bulletin ID. Each folder must contain both update metadata and required binaries.
        
        :param updateID: The update to be installed on the host.
        
        :param force: Specify whether to force reinstall an update. By default, installing an already-installed update would fail with the PatchAlreadyInstalled fault. If force is set to true, the update will be forcifully reinstalled, thus overwriting the already installed update.
        
        '''
        return self.delegate("InstallHostPatch_Task")(repository, updateID, force)
    
    def InstallHostPatchV2_Task(self, metaUrls=None, bundleUrls=None, vibUrls=None, spec=None):
        '''Patch the host. The operation is not cancelable. If the patch installation
        failed, an atomic rollback of the installation will be attempted. Manual
        rollback is required if the atomic rollback failed, see PatchInstallFailed for
        details.
        
        :param metaUrls: A list of urls pointing to metadata.zip.
        
        :param bundleUrls: a list of urls pointing to an "offline" bundle.
        
        :param vibUrls: The urls of update binary files to be installed.
        
        :param spec: 
        
        '''
        return self.delegate("InstallHostPatchV2_Task")(metaUrls, bundleUrls, vibUrls, spec)
    
    def QueryHostPatch_Task(self, spec=None):
        '''Query the host for installed bulletins.
        
        :param spec: 
        
        '''
        return self.delegate("QueryHostPatch_Task")(spec)
    
    def ScanHostPatch_Task(self, repository, updateID=None):
        '''<b>Deprecated.</b> <i>As of VI API 4.0, use ScanHostPatchV2_Task.</i> Scan the
        host for the patch status. The operation is cancelable through the returned
        Task object. Integrity checks are performed on the metadata only during the
        scan operation.
        
        :param repository: Location of the repository that contains the bulletin depot. The depot must be organized as a flat collection of bulletins with each one being a folder named after the bulletin ID. Each folder must contain the full update metadata.
        
        :param updateID: The updates to scan. Wildcards can be used to specify the update IDs. The wildcards will be expanded to include all updates whose IDs match the specified wildcard and whose metadata is available in the repository. Specifying no update is equivalent to a wildcard "*". In this case all updates available in the repository will be scanned.
        
        '''
        return self.delegate("ScanHostPatch_Task")(repository, updateID)
    
    def ScanHostPatchV2_Task(self, metaUrls=None, bundleUrls=None, spec=None):
        '''Scan the host for the patch status. The operation is cancelable through the
        returned Task object. Integrity checks are performed on the metadata only
        during the scan operation.
        
        :param metaUrls: a list of urls pointing to metadata.zip.
        
        :param bundleUrls: a list of urls pointing to an "offline" bundle.
        
        :param spec: 
        
        '''
        return self.delegate("ScanHostPatchV2_Task")(metaUrls, bundleUrls, spec)
    
    def StageHostPatch_Task(self, metaUrls=None, bundleUrls=None, vibUrls=None, spec=None):
        '''Stage the vib files to esx local location and possibly do some run time check.
        
        :param metaUrls: A list of urls pointing to metadata.zip.
        
        :param bundleUrls: a list of urls pointing to an "offline" bundle.
        
        :param vibUrls: The urls of update binary files to be staged.
        
        :param spec: 
        
        '''
        return self.delegate("StageHostPatch_Task")(metaUrls, bundleUrls, vibUrls, spec)
    
    def UninstallHostPatch_Task(self, bulletinIds=None, spec=None):
        '''Uninstall patch from the host. The operation is not cancelable.
        
        :param bulletinIds: A list of bulletin IDs to be removed.
        
        :param spec: 
        
        '''
        return self.delegate("UninstallHostPatch_Task")(bulletinIds, spec)