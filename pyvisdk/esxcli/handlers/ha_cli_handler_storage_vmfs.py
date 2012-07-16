
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageVmfs(Base):
    '''
    VMFS operations.
    '''
    moid = 'ha-cli-handler-storage-vmfs'
    def upgrade(self, volumelabel=None, volumeuuid=None):
        '''
        Upgrade a VMFS3 volume to VMFS5.
        :param volumelabel: string, The label of the volume to upgrade.
        :param volumeuuid: string, The uuid of the volume to upgrade.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.vmfs.Upgrade',
                            volumelabel=volumelabel,
                            volumeuuid=volumeuuid,
                            )   