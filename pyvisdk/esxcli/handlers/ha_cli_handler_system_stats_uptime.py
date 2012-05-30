
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemStatsUptime(Base):
    '''
    System uptime, in microseconds
    '''
    moid = 'ha-cli-handler-system-stats-uptime'
    def get(self):
        '''
        Disply the number of microseconds the system has been running.
        :returns: long
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.stats.uptime.Get',
                            )   