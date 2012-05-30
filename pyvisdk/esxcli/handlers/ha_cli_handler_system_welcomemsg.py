
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemWelcomemsg(Base):
    '''
    Commands to get and set the welcome banner for DCUI.
    '''
    moid = 'ha-cli-handler-system-welcomemsg'
    def set(self, message):
        '''
        Set the Welcome Message for DCUI.
        :param message: string, Welcome Message String.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.welcomemsg.Set',
                            message=message,
                            )
    def get(self):
        '''
        Get the Welcome Message for DCUI.
        :returns: string
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.welcomemsg.Get',
                            )   