
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemSyslogConfigLogger(Base):
    '''
    Operations for sub-loggers
    '''
    moid = 'ha-cli-handler-system-syslog-config-logger'
    def set(self, id, reset=None, rotate=None, size=None):
        '''
        Set configuration options for a specific sub-logger
        :param id: string, The id of the logger to configure
        :param reset: string, Reset values to default
        :param rotate: long, Number of rotated logs to keep for a specific logger (requires --id)
        :param size: long, Set size of logs before rotation for a specific logger, in KiB (requires --id)
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.syslog.config.logger.Set',
                            id=id,
                            reset=reset,
                            rotate=rotate,
                            size=size,
                            )
    def list(self):
        '''
        Show the currently configured sub-loggers
        :returns: vim.EsxCLI.system.syslog.config.logger.list.LoggerConfiguration[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.syslog.config.logger.List',
                            )   