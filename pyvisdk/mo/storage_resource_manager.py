
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class StorageResourceManager(BaseEntity):
    '''This managed object type provides a way to configure resource usage for storage
    resources.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.StorageResourceManager):
        super(StorageResourceManager, self).__init__(core, name=name, ref=ref, type=type)

    

    
    
    def ApplyStorageDrsRecommendation_Task(self, key):
        '''Applies a recommendation from the recommendation list. Each recommendation can
        be applied only once. In the case of CreateVm and CloneVm a VirtualMachine is
        returned. Other workflows don't have a return value.Applies a recommendation
        from the recommendation list. Each recommendation can be applied only once. In
        the case of CreateVm and CloneVm a VirtualMachine is returned. Other workflows
        don't have a return value.Applies a recommendation from the recommendation
        list. Each recommendation can be applied only once. In the case of CreateVm and
        CloneVm a VirtualMachine is returned. Other workflows don't have a return
        value.
        
        :param key: The key fields of the Recommendations that are applied.
        
        '''
        return self.delegate("ApplyStorageDrsRecommendation_Task")(key)
    
    def ApplyStorageDrsRecommendationToPod_Task(self, pod, key):
        '''Applies a recommendation from the recommendation list. Each recommendation can
        be applied only once.Applies a recommendation from the recommendation list.
        Each recommendation can be applied only once.
        
        :param pod: The storage pod.
        
        :param key: The key field of the Recommendation.
        
        '''
        return self.delegate("ApplyStorageDrsRecommendationToPod_Task")(pod, key)
    
    def CancelStorageDrsRecommendation(self, key):
        '''Cancels a recommendation. Currently only initial placement recommendations can
        be cancelled. Migration recommendations cannot.
        
        :param key: The key field of the Recommendation.
        
        '''
        return self.delegate("CancelStorageDrsRecommendation")(key)
    
    def ConfigureDatastoreIORM_Task(self, datastore, spec):
        '''Changes configuration of storage I/O resource management for a given datastore.
        The changes are applied to all the backing storage devices for the datastore.
        Currently we only support storage I/O resource management on VMFS volumes. In
        order to enable storage I/O resource management on a datstore, we require that
        all the hosts that are attached to the datastore support this feature.Changes
        configuration of storage I/O resource management for a given datastore. The
        changes are applied to all the backing storage devices for the datastore.
        Currently we only support storage I/O resource management on VMFS volumes. In
        order to enable storage I/O resource management on a datstore, we require that
        all the hosts that are attached to the datastore support this feature.
        
        :param datastore: The datastore to be configured.
        
        :param spec: The configuration spec.
        
        '''
        return self.delegate("ConfigureDatastoreIORM_Task")(datastore, spec)
    
    def ConfigureStorageDrsForPod_Task(self, pod, spec, modify):
        '''Change the storage DRS configuration for a pod StoragePod.
        
        :param pod: The storage pod.
        
        :param spec: A set of storage Drs configuration changes to apply to the storage pod. The specification can be a complete set of changes or a partial set of changes, applied incrementally.
        
        :param modify: Flag to specify whether the specification ("spec") should be applied incrementally. If "modify" is false and the operation succeeds, then the configuration of the storage pod matches the specification exactly; in this case any unset portions of the specification will result in unset or default portions of the configuration.
        
        '''
        return self.delegate("ConfigureStorageDrsForPod_Task")(pod, spec, modify)
    
    def QueryIORMConfigOption(self, host):
        '''Query configuration options for storage I/O resource management.
        
        :param host: [in] - The host VC will forward the query to. This parameter is ignored by host if this method is called on a host directly.
        
        '''
        return self.delegate("QueryIORMConfigOption")(host)
    
    def RecommendDatastores(self, storageSpec):
        '''This method returns a StoragePlacementResult object. This API is intended to
        replace the following existing APIs for SDRS-enabled pods: CreateVm:
        StoragePlacementSpec::type == create = CreateVM_Task AddDisk:
        StoragePlacementSpec::type == reconfigure = ReconfigVM_Task RelocateVm:
        StoragePlacementSpec::type == relocate = RelocateVM_Task CloneVm:
        StoragePlacementSpec::type == clone = CloneVM_Task The PodSelectionSpec
        parameter in StoragePlacementSpec is required for all workflows. It specifies
        which SDRS-enabled pod the user has selected for the VM and/or for each disk.
        For CreateVm, RelocateVm and CloneVm, PodSelectionSpec.storagePod is the user
        selected SDRS pod for the VM, i.e., its system files. For all workflows,
        PodSelectionSpec.disk.storagePod is the user selected SDRS pod for the given
        disk. Note that a DiskLocator must be specified for each disk that the user
        requests to create, migrate or clone into an SDRS pod, even if it's the same
        pod as the VM or the user has manually selected a datastore within the pod. If
        the user has manually selected a datastore, the datastore must be specified in
        the workflow specific fields as described below. For CreateVm and AddDisk, the
        manually selected datastore must be specified in ConfigSpec.files or
        ConfigSpec.deviceChange.device.backing.datastore, the fields should will be
        unset if the user wants SDRS to recommend the datastore. For RelocateVm, the
        manually selected datastore must be specified in RelocateSpec.datastore or
        RelocateSpec.disk.datastore; the fields should be unset iff the user wants SDRS
        recommendations. For CloneVm, the manually selected datastore must be specified
        in CloneSpec.location.datastore or CloneSpec.location.disk[].datastore; the
        fields should be unset iff the user wants SDRS recommendations. The remaining
        expected input parameters in StoragePlacementSpec will be the same as those for
        the existing API as determined by StoragePlacementSpec::type. If a parameter is
        optional in the existing API, it will also be optional in the new API.This
        method returns a StoragePlacementResult object. This API is intended to replace
        the following existing APIs for SDRS-enabled pods: CreateVm:
        StoragePlacementSpec::type == create = CreateVM_Task AddDisk:
        StoragePlacementSpec::type == reconfigure = ReconfigVM_Task RelocateVm:
        StoragePlacementSpec::type == relocate = RelocateVM_Task CloneVm:
        StoragePlacementSpec::type == clone = CloneVM_Task The PodSelectionSpec
        parameter in StoragePlacementSpec is required for all workflows. It specifies
        which SDRS-enabled pod the user has selected for the VM and/or for each disk.
        For CreateVm, RelocateVm and CloneVm, PodSelectionSpec.storagePod is the user
        selected SDRS pod for the VM, i.e., its system files. For all workflows,
        PodSelectionSpec.disk.storagePod is the user selected SDRS pod for the given
        disk. Note that a DiskLocator must be specified for each disk that the user
        requests to create, migrate or clone into an SDRS pod, even if it's the same
        pod as the VM or the user has manually selected a datastore within the pod. If
        the user has manually selected a datastore, the datastore must be specified in
        the workflow specific fields as described below. For CreateVm and AddDisk, the
        manually selected datastore must be specified in ConfigSpec.files or
        ConfigSpec.deviceChange.device.backing.datastore, the fields should will be
        unset if the user wants SDRS to recommend the datastore. For RelocateVm, the
        manually selected datastore must be specified in RelocateSpec.datastore or
        RelocateSpec.disk.datastore; the fields should be unset iff the user wants SDRS
        recommendations. For CloneVm, the manually selected datastore must be specified
        in CloneSpec.location.datastore or CloneSpec.location.disk[].datastore; the
        fields should be unset iff the user wants SDRS recommendations. The remaining
        expected input parameters in StoragePlacementSpec will be the same as those for
        the existing API as determined by StoragePlacementSpec::type. If a parameter is
        optional in the existing API, it will also be optional in the new API.This
        method returns a StoragePlacementResult object. This API is intended to replace
        the following existing APIs for SDRS-enabled pods: CreateVm:
        StoragePlacementSpec::type == create = CreateVM_Task AddDisk:
        StoragePlacementSpec::type == reconfigure = ReconfigVM_Task RelocateVm:
        StoragePlacementSpec::type == relocate = RelocateVM_Task CloneVm:
        StoragePlacementSpec::type == clone = CloneVM_Task The PodSelectionSpec
        parameter in StoragePlacementSpec is required for all workflows. It specifies
        which SDRS-enabled pod the user has selected for the VM and/or for each disk.
        For CreateVm, RelocateVm and CloneVm, PodSelectionSpec.storagePod is the user
        selected SDRS pod for the VM, i.e., its system files. For all workflows,
        PodSelectionSpec.disk.storagePod is the user selected SDRS pod for the given
        disk. Note that a DiskLocator must be specified for each disk that the user
        requests to create, migrate or clone into an SDRS pod, even if it's the same
        pod as the VM or the user has manually selected a datastore within the pod. If
        the user has manually selected a datastore, the datastore must be specified in
        the workflow specific fields as described below. For CreateVm and AddDisk, the
        manually selected datastore must be specified in ConfigSpec.files or
        ConfigSpec.deviceChange.device.backing.datastore, the fields should will be
        unset if the user wants SDRS to recommend the datastore. For RelocateVm, the
        manually selected datastore must be specified in RelocateSpec.datastore or
        RelocateSpec.disk.datastore; the fields should be unset iff the user wants SDRS
        recommendations. For CloneVm, the manually selected datastore must be specified
        in CloneSpec.location.datastore or CloneSpec.location.disk[].datastore; the
        fields should be unset iff the user wants SDRS recommendations. The remaining
        expected input parameters in StoragePlacementSpec will be the same as those for
        the existing API as determined by StoragePlacementSpec::type. If a parameter is
        optional in the existing API, it will also be optional in the new API.This
        method returns a StoragePlacementResult object. This API is intended to replace
        the following existing APIs for SDRS-enabled pods: CreateVm:
        StoragePlacementSpec::type == create = CreateVM_Task AddDisk:
        StoragePlacementSpec::type == reconfigure = ReconfigVM_Task RelocateVm:
        StoragePlacementSpec::type == relocate = RelocateVM_Task CloneVm:
        StoragePlacementSpec::type == clone = CloneVM_Task The PodSelectionSpec
        parameter in StoragePlacementSpec is required for all workflows. It specifies
        which SDRS-enabled pod the user has selected for the VM and/or for each disk.
        For CreateVm, RelocateVm and CloneVm, PodSelectionSpec.storagePod is the user
        selected SDRS pod for the VM, i.e., its system files. For all workflows,
        PodSelectionSpec.disk.storagePod is the user selected SDRS pod for the given
        disk. Note that a DiskLocator must be specified for each disk that the user
        requests to create, migrate or clone into an SDRS pod, even if it's the same
        pod as the VM or the user has manually selected a datastore within the pod. If
        the user has manually selected a datastore, the datastore must be specified in
        the workflow specific fields as described below. For CreateVm and AddDisk, the
        manually selected datastore must be specified in ConfigSpec.files or
        ConfigSpec.deviceChange.device.backing.datastore, the fields should will be
        unset if the user wants SDRS to recommend the datastore. For RelocateVm, the
        manually selected datastore must be specified in RelocateSpec.datastore or
        RelocateSpec.disk.datastore; the fields should be unset iff the user wants SDRS
        recommendations. For CloneVm, the manually selected datastore must be specified
        in CloneSpec.location.datastore or CloneSpec.location.disk[].datastore; the
        fields should be unset iff the user wants SDRS recommendations. The remaining
        expected input parameters in StoragePlacementSpec will be the same as those for
        the existing API as determined by StoragePlacementSpec::type. If a parameter is
        optional in the existing API, it will also be optional in the new API.
        
        :param storageSpec: 
        
        '''
        return self.delegate("RecommendDatastores")(storageSpec)
    
    def RefreshStorageDrsRecommendation(self, pod):
        '''Make Storage DRS invoke again on the specified pod StoragePod and return a new
        list of recommendations. Concurrent "refresh" requests may be combined together
        and trigger only one Storage DRS invocation.
        
        :param pod: The storage pod. The recommendations generated is stored at PodStorageDrsEntry#recommendation.
        
        '''
        return self.delegate("RefreshStorageDrsRecommendation")(pod)