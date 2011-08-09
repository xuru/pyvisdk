
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDatastoreSystemCapabilities(DynamicData):
    '''Capability vector indicating the available product features.
    '''
    
    def __init__(self, localDatastoreSupported, nfsMountCreationRequired, nfsMountCreationSupported, vmfsExtentExpansionSupported):
        # MUST define these
        super(HostDatastoreSystemCapabilities, self).__init__()
    
        self.data['localDatastoreSupported'] = localDatastoreSupported
        self.data['nfsMountCreationRequired'] = nfsMountCreationRequired
        self.data['nfsMountCreationSupported'] = nfsMountCreationSupported
        self.data['vmfsExtentExpansionSupported'] = vmfsExtentExpansionSupported
    
    
    @property
    def localDatastoreSupported(self):
        '''Indicates whether local datastores are supported.
        '''
        return self.data['localDatastoreSupported']

    @property
    def nfsMountCreationRequired(self):
        '''Indicates whether mounting the NFS volume is required to be done as part of NAS
        datastore creation. If this is set to true, then NAS datastores cannot be
        created for currently mounted NFS volumes.
        '''
        return self.data['nfsMountCreationRequired']

    @property
    def nfsMountCreationSupported(self):
        '''Indicates whether mounting an NFS volume is supported when a NAS datastore is
        created. If this option is false, then NAS datastores corresponding to NFS
        volumes can be created only for already mounted NFS volumes.
        '''
        return self.data['nfsMountCreationSupported']

    @property
    def vmfsExtentExpansionSupported(self):
        '''Indicates whether vmfs extent expansion is supported.
        '''
        return self.data['vmfsExtentExpansionSupported']

