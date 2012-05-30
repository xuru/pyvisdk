
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class HardwareClock(Base):
    '''
    Interaction with the hardware clock.
    '''
    moid = 'ha-cli-handler-hardware-clock'
    def set(self, day=None, hour=None, min=None, month=None, sec=None, year=None):
        '''
        Set the hardware clock time. Any missing parameters will default to the current time.
        :param day: long, Day
        :param hour: long, Hour
        :param min: long, Minute
        :param month: long, Month
        :param sec: long, Second
        :param year: long, Year
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.hardware.clock.Set',
                            day=day,
                            hour=hour,
                            min=min,
                            month=month,
                            sec=sec,
                            year=year,
                            )
    def get(self):
        '''
        Disply the current hardware clock time.
        :returns: string
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.hardware.clock.Get',
                            )   