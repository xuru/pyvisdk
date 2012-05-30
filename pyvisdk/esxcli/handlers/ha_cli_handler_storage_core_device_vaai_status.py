
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageCoreDeviceVaaiStatus(Base):
    '''
    Query a SCSI device's VAAI state.
    '''
    moid = 'ha-cli-handler-storage-core-device-vaai-status'
    def get(self, device=None):
        '''
        List VAAI properties for devices currently registered with the PSA.
        :param device: string, Filter the output of this command to only show a single device.
        :returns: vim.EsxCLI.storage.core.device.vaai.status.get.ScsiDevice[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.device.vaai.status.Get',
                            device=device,
                            )   