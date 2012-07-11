
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemProcess(Base):
    '''
    Commands relating to running processes.
    '''
    moid = 'ha-cli-handler-system-process'
    def list(self):
        '''
        List the VMkernel UserWorld processes currently on the host.
        :returns: vim.EsxCLI.system.process.list.UserWorld[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.process.List',
                            )   