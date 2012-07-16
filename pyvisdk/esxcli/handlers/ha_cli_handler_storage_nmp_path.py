
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageNmpPath(Base):
    '''
    Operations pertaining to the paths currently claimed by the VMware Native Multipath Plugin.
    '''
    moid = 'ha-cli-handler-storage-nmp-path'
    def list(self, device=None, path=None):
        '''
        List the paths currently claimed by the VMware NMP Multipath Plugin and show the SATP and PSP information associated with that path.
        :param device: string, Filter the output of this command to only show paths to a single device.
        :param path: string, Filter the output of this command to only show a single path.
        :returns: vim.EsxCLI.storage.nmp.path.list.ScsiPath[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nmp.path.List',
                            device=device,
                            path=path,
                            )   