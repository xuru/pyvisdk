
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemTime(Base):
    '''
    Commands to get and set system time.
    '''
    moid = 'ha-cli-handler-system-time'
    def set(self, day=None, hour=None, min=None, month=None, sec=None, year=None):
        '''
        Set the system clock time. Any missing parameters will default to the current time
        :param day: long, Day
        :param hour: long, Hour
        :param min: long, Minute
        :param month: long, Month
        :param sec: long, Second
        :param year: long, Year
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.time.Set',
                            day=day,
                            hour=hour,
                            min=min,
                            month=month,
                            sec=sec,
                            year=year,
                            )
    def get(self):
        '''
        Disply the current system time.
        :returns: string
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.time.Get',
                            )   