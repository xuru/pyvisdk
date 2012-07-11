
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageCorePlugin(Base):
    '''
    Operations pertaining to the pluggable storage architectures' plugins. The operation currently allowed is to list the available plugins on the system with the type of those plugins
    '''
    moid = 'ha-cli-handler-storage-core-plugin'
    def list(self, pluginclass=None):
        '''
        List loaded PSA plugins on the system.
        :param pluginclass: string, Indicate the class of plugin to limit the list to.  Allowed values are :
    Filter: Filter plugins
    MP: MultiPathing plugins
    VAAI: VAAI plugins
    all: All PSA Plugins (default)

        :returns: vim.EsxCLI.storage.core.plugin.list.PsaPlugin[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.plugin.List',
                            pluginclass=pluginclass,
                            )   