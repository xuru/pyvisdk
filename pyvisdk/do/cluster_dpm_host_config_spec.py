
from pyvisdk.do.array_update_spec import ArrayUpdateSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterDpmHostConfigSpec(ArrayUpdateSpec):
    '''The ClusterDpmHostConfigSpec data object provides information that the Server uses
        to update the DPM configuration for a single host (identified by the key
        property). The host DPM configuration overrides the cluster default DPM
        setting (ClusterConfigSpecEx.dpmConfig).The vSphere API defines three
        update operations (ArrayUpdateSpec.operation).* add: Define DPM behavior
        for a host. If the cluster configuration already includes a DPM behavior
        override for the specified host, this operation removes the existing
        override and adds the new one. The new DPM override will use the cluster
        default value if you do not specify the behavior property
        (defaultDpmBehavior). * edit: Perform an incremental update to an existing
        DPM configuration entry for a host. The reconfigure method changes only
        the properties that you set in the data object. The entry must exist in
        the ClusterConfigSpecEx.dpmHostConfigSpec array. * remove: Remove the DPM
        override for the specified host. To identify the host to delete, use the
        removeKey property to specify the key in the host override.Use the
        ReconfigureComputeResource_Task method to update the DPM configuration. If
        you set the modify parameter to true, you can use any of the three
        operations (add, edit, or remove). If you set the modify parameter to
        false, you can use only the add operation.
    '''
    
    def __init__(self, info):
        # MUST define these
        super(ClusterDpmHostConfigSpec, self).__init__()
    
        self.data['info'] = info
    
    
    @property
    def info(self):
        '''
        '''
        return self.data['info']

