
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemSettingsKeyboardLayout(Base):
    '''
    Operations that relate to keyboard layout
    '''
    moid = 'ha-cli-handler-system-settings-keyboard-layout'
    def set(self, layout=None, nopersist=None):
        '''
        Set the keyboard layout
        :param layout: string, The name of the layout to set
        :param nopersist: boolean, Only apply this layout for the current boot
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.settings.keyboard.layout.Set',
                            layout=layout,
                            nopersist=nopersist,
                            )
    def list(self):
        '''
        List the keyboard layout
        :returns: vim.EsxCLI.system.settings.keyboard.layout.list.Layout[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.settings.keyboard.layout.List',
                            )
    def get(self):
        '''
        Get the keyboard layout
        :returns: string
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.settings.keyboard.layout.Get',
                            )   