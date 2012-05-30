
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageCoreDeviceWorld(Base):
    '''
    Operations on worlds pertaining to the pluggable storage architectures' logical devices on the system. 
    '''
    moid = 'ha-cli-handler-storage-core-device-world'
    def list(self, device=None):
        '''
        Get a list of the worlds that are currently using devices on the ESX host.
        :param device: string, Filter the output of the command to limit the output to a specific device.  This device name can be any of the UIDs registered for a device.
        :returns: vim.EsxCLI.storage.core.device.world.list.ScsiDeviceWorld[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.device.world.List',
                            device=device,
                            )   