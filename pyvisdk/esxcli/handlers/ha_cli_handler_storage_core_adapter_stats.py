
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageCoreAdapterStats(Base):
    '''
    Stats operations on SCSI Host Bus Adapters on the system.
    '''
    moid = 'ha-cli-handler-storage-core-adapter-stats'
    def get(self, adapter=None):
        '''
        List the SCSI stats for the SCSI Host Bus Adapters in the system.
        :param adapter: string, Limit the stats output to one adapter
        :returns: vim.EsxCLI.storage.core.adapter.stats.get.ScsiAdapterStats[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.adapter.stats.Get',
                            adapter=adapter,
                            )   