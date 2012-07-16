
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageNmpPspGenericPathconfig(Base):
    '''
    PSP path configuration operations
    '''
    moid = 'ha-cli-handler-storage-nmp-psp-generic-pathconfig'
    def set(self, config, path):
        '''
        Allow setting of per path PSP configuration parameters.  This command will set the configuration for the given path with whichever PSP it is currently configurated with.
        :param config: string, The configuration string you wish to set.
        :param path: string, The path you wish to set PSP configuration for.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nmp.psp.generic.pathconfig.Set',
                            config=config,
                            path=path,
                            )
    def get(self, path):
        '''
        Allow retrieving of per path PSP configuration parameters.
        :param path: string, The path you wish to get PSP configuration for.
        :returns: string
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nmp.psp.generic.pathconfig.Get',
                            path=path,
                            )   