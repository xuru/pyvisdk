
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageCorePathStats(Base):
    '''
    Stats operations pertaining to the pluggable storage architectures' device paths on the system. 
    '''
    moid = 'ha-cli-handler-storage-core-path-stats'
    def get(self, path=None):
        '''
        List the SCSI stats for the SCSI Paths in the system.
        :param path: string, Limit the stats output to one specific path. This path name can be the runtime name or the path UID.
        :returns: vim.EsxCLI.storage.core.path.stats.get.ScsiPathStats[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.path.stats.Get',
                            path=path,
                            )   