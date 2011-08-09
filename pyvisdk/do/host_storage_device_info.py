
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostStorageDeviceInfo(DynamicData):
    '''This data object type describes the storage subsystem configuration.
    '''
    
    def __init__(self, hostBusAdapter, multipathInfo, plugStoreTopology, scsiLun, scsiTopology, softwareInternetScsiEnabled):
        # MUST define these
        super(HostStorageDeviceInfo, self).__init__()
    
        self.data['hostBusAdapter'] = hostBusAdapter
        self.data['multipathInfo'] = multipathInfo
        self.data['plugStoreTopology'] = plugStoreTopology
        self.data['scsiLun'] = scsiLun
        self.data['scsiTopology'] = scsiTopology
        self.data['softwareInternetScsiEnabled'] = softwareInternetScsiEnabled
    
    
    @property
    def hostBusAdapter(self):
        '''The list of host bus adapters available on the host.
        '''
        return self.data['hostBusAdapter']

    @property
    def multipathInfo(self):
        '''The multipath configuration that controls multipath policy for ScsiLuns. This data
        object exists only if path information is available and is configurable.
        '''
        return self.data['multipathInfo']

    @property
    def plugStoreTopology(self):
        '''The plug-store topology on the host system. This data object exists only if the
        plug-store system is available and configurable.
        '''
        return self.data['plugStoreTopology']

    @property
    def scsiLun(self):
        '''The list of SCSI logical units available on the host.
        '''
        return self.data['scsiLun']

    @property
    def scsiTopology(self):
        '''Storage topology view of SCSI storage devices. This data object exists only if
        storage topology information is available. See the ScsiTopology data
        object type for more information.
        '''
        return self.data['scsiTopology']

    @property
    def softwareInternetScsiEnabled(self):
        '''Indicates if the software iSCSI initiator is enabled on this system
        '''
        return self.data['softwareInternetScsiEnabled']

