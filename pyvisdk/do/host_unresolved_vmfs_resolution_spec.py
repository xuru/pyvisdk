
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostUnresolvedVmfsResolutionSpec(DynamicData):
    '''An unresolved VMFS volume is reported when one or more device partitions of volume
        are detected to have copies of extents of the volume. Such copies can be
        created via replication or snapshots, for example. This data object type
        describes how to resolve an unbound VMFS volume. The SCSI device path for
        each of the VMFS volume extent should be specified. For the current
        release, only head-extent needs to be specified. In future releases, we
        will allow user to specify explicitly all the extents which makes up a new
        Vmfs Volume.
    '''
    
    def __init__(self, extentDevicePath, uuidResolution):
        # MUST define these
        super(HostUnresolvedVmfsResolutionSpec, self).__init__()
    
        self.data['extentDevicePath'] = extentDevicePath
        self.data['uuidResolution'] = uuidResolution
    
    
    @property
    def extentDevicePath(self):
        '''List of device paths each specifying a VMFS extent.
        '''
        return self.data['extentDevicePath']

    @property
    def uuidResolution(self):
        '''When set to Resignature, new Uuid is assigned to the VMFS volume. When set to
        'forceMount', existing uuid is assigned to the Vmfs volume and Vmfs
        volumes metadata doesn't change.
        '''
        return self.data['uuidResolution']

