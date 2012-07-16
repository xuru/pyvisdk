
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemProcessStatsRunning(Base):
    '''
    Number of currently running worlds
    '''
    moid = 'ha-cli-handler-system-process-stats-running'
    def get(self):
        '''
        Number of currently running processes.
        :returns: vim.EsxCLI.system.process.stats.running.get.ProcessStatsRunningGet
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.process.stats.running.Get',
                            )   