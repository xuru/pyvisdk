
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageCoreDeviceStats(Base):
    '''
    Stats operations pertaining to the pluggable storage architectures' logical devices on the system. 
    '''
    moid = 'ha-cli-handler-storage-core-device-stats'
    def get(self, device=None):
        '''
        List the SCSI stats for SCSI Devices in the system.
        :param device: string, Limit the stats output to one specific device. This device name can be any of the UIDs the device reports
        :returns: vim.EsxCLI.storage.core.device.stats.get.ScsiDeviceStats[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.device.stats.Get',
                            device=device,
                            )   