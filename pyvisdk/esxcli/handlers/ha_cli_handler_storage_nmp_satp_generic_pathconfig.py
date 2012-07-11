
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageNmpSatpGenericPathconfig(Base):
    '''
    SATP path configuration operations
    '''
    moid = 'ha-cli-handler-storage-nmp-satp-generic-pathconfig'
    def set(self, config, path):
        '''
        Allow setting of per path SATP configuration parameters.  This command will set the configuration for the given path with whichever SATP it is currently configurated with.
        :param config: string, The configuration string you wish to set.
        :param path: string, The path you wish to set SATP configuration for.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nmp.satp.generic.pathconfig.Set',
                            config=config,
                            path=path,
                            )
    def get(self, path):
        '''
        Allow retrieving of per path SATP configuration parameters.
        :param path: string, The path you wish to get SATP configuration for.
        :returns: string
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nmp.satp.generic.pathconfig.Get',
                            path=path,
                            )   