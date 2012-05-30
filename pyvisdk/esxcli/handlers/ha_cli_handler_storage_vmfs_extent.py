
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageVmfsExtent(Base):
    '''
    Manage VMFS extents.
    '''
    moid = 'ha-cli-handler-storage-vmfs-extent'
    def list(self):
        '''
        List the VMFS extents available on the host.
        :returns: vim.EsxCLI.storage.vmfs.extent.list.FilesystemVMFSExtents[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.vmfs.extent.List',
                            )   