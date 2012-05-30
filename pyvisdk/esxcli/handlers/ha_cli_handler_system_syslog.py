
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemSyslog(Base):
    '''
    Operations relating to system logging
    '''
    moid = 'ha-cli-handler-system-syslog'
    def reload(self):
        '''
        Reload the log daemon to apply any new configuration options
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.syslog.Reload',
                            )
    def mark(self, message):
        '''
        Mark all logs with the specified string
        :param message: string, The message to place in the logs
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.syslog.Mark',
                            message=message,
                            )   