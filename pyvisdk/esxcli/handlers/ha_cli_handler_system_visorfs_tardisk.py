
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemVisorfsTardisk(Base):
    '''
    Operations pertaining to visorfs tardisks.
    '''
    moid = 'ha-cli-handler-system-visorfs-tardisk'
    def list(self):
        '''
        List the tardisks used by the host.
        :returns: vim.EsxCLI.system.visorfs.tardisk.list.VisorfsTardisk[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.visorfs.tardisk.List',
                            )   