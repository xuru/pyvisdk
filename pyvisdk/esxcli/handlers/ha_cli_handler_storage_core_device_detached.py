
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageCoreDeviceDetached(Base):
    '''
    Operations pertaining to the pluggable storage architectures' detached logical devices on the system.
    '''
    moid = 'ha-cli-handler-storage-core-device-detached'
    def list(self, device=None):
        '''
        Lists all devices that were detached manually by changing their state on the system.
        :param device: string, Filter the output of the command to limit the output to a specific device.
        :returns: vim.EsxCLI.storage.core.device.detached.list.ScsiDetachedDeviceListMap[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.device.detached.List',
                            device=device,
                            )
    def remove(self, device):
        '''
        Provide control to allow a user to remove Detached devices from the persistent detached device list.
        :param device: string, Select the detached device to remove from the Detached Device List.
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.device.detached.Remove',
                            device=device,
                            )   