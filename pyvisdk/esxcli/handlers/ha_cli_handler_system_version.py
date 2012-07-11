
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemVersion(Base):
    '''
    Commands to get version information.
    '''
    moid = 'ha-cli-handler-system-version'
    def get(self):
        '''
        Display the product name, version and build information.
        :returns: vim.EsxCLI.system.version.get.VersionGet
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.version.Get',
                            )   