
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemSyslogConfig(Base):
    '''
    Operations relating to system logging configuration
    '''
    moid = 'ha-cli-handler-system-syslog-config'
    def set(self, defaultrotate=None, defaultsize=None, logdir=None, logdirunique=None, loghost=None, reset=None):
        '''
        Set global log configuration options
        :param defaultrotate: long, Default number of rotated logs to keep
        :param defaultsize: long, Default size of logs before rotation, in KiB
        :param logdir: string, The directory to output logs to
        :param logdirunique: boolean, Place logs in a unique subdirectory of logdir, based on hostname
        :param loghost: string, The remote host to output logs to
        :param reset: string, Reset values to default
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.syslog.config.Set',
                            defaultrotate=defaultrotate,
                            defaultsize=defaultsize,
                            logdir=logdir,
                            logdirunique=logdirunique,
                            loghost=loghost,
                            reset=reset,
                            )
    def get(self):
        '''
        Show the current global configuration values
        :returns: vim.EsxCLI.system.syslog.config.get.SyslogConfiguration
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.syslog.config.Get',
                            )   