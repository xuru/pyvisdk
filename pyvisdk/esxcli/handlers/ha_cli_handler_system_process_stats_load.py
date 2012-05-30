
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemProcessStatsLoad(Base):
    '''
    System load averages
    '''
    moid = 'ha-cli-handler-system-process-stats-load'
    def get(self):
        '''
        System load average over the last 1, 5 and 15 minutes.
        :returns: vim.EsxCLI.system.process.stats.load.get.ProcessStatsLoadGet
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.process.stats.load.Get',
                            )   