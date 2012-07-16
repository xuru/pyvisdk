
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class EsxcliCommand(Base):
    '''
    Operations to get information about commands.
    '''
    moid = 'ha-cli-handler-esxcli-command'
    def list(self):
        '''
        This command will list all of the esxcli commands with their namespace, object, command name and description.
        :returns: vim.EsxCLI.esxcli.command.list.EsxCliCommand[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.esxcli.command.List',
                            )   