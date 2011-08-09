
from pyvisdk.do.array_update_spec import ArrayUpdateSpec
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterDrsVmConfigSpec(ArrayUpdateSpec):
    '''Updates the per-virtual-machine DRS configuration.To update the DRS configuration
        of a virtual machine, a copy of this object is included in the
        ClusterConfigSpecEx object passed to the method
        ReconfigureComputeResource_Task.If is used to incrementally update the
        cluster configuration (i.e., the parameter is true), then three operations
        are provided for updating the DRS configuration for a virtual machine.
        These operations are listed below (see ArrayUpdateSpec for more
        information on these operations).* add: add a configuration for the
        virtual machine, overwritting the existing configuration if one exists *
        edit: incrmentally update the existing configuration; an existing
        configuration must exist * remove: remove the existing configuration; an
        existing configuration must existIf, instead, this method is used to
        overwrite the cluster configuration (i.e., the parameter is false) thereby
        creating a new configuration, only the add operation is allowed. In this
        case, creates a DRS configuration for a virtual machine in the new cluster
        configuration.
    '''
    
    def __init__(self, info):
        # MUST define these
        super(ClusterDrsVmConfigSpec, self).__init__()
    
        self.data['info'] = info
    
    
    @property
    def info(self):
        '''
        '''
        return self.data['info']

