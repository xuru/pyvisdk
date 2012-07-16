
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageCoreDevicePartition(Base):
    '''
    Stats operations pertaining to the pluggable storage architectures' logical devices on the system. 
    '''
    moid = 'ha-cli-handler-storage-core-device-partition'
    def list(self, device=None):
        '''
        For a given device list all of the partitions
        :param device: string, Filter the output to a specific device.
        :returns: vim.EsxCLI.storage.core.device.partition.list.ScsiDevicePartition[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.device.partition.List',
                            device=device,
                            )   