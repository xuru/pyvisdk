
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostMultipathInfo(DynamicData):
    '''This data object type describes the multipathing policy configuration to determine
        the storage failover policies for a SCSI logical unit. The multipathing
        policy configuration operates on SCSI logical units and the paths to the
        logical units.Multipath policy configuration is only possible on storage
        devices provided by the native multipathing plug-store plugin. Storage
        devices using the native multipathing storage plugin will have an entry in
        this data object. Storage devices provided by a different storage plugin
        will not appear in the inventory represented by this data object.Legacy
        note: In hosts where HostMultipathStateInfo is not defined or does not
        exist on the HostStorageDeviceInfo object, only native multipathing
        exists. That means for these hosts, the MultipathInfo object contains the
        complete set of LUNs and paths on the LUNs available on the host.
    '''
    
    def __init__(self, lun):
        # MUST define these
        super(HostMultipathInfo, self).__init__()
    
        self.data['lun'] = lun
    
    
    @property
    def lun(self):
        '''List of logical units that can be configured for multipathing.
        '''
        return self.data['lun']

