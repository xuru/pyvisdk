
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemSettingsKernel(Base):
    '''
    Operations that allow viewing and manipulation of system kernel settings.
    '''
    moid = 'ha-cli-handler-system-settings-kernel'
    def set(self, setting, value):
        '''
        Set a VMKernel setting.
        :param setting: string, The name of the VMKernel setting to set.
        :param value: string, The value to set the setting to.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.settings.kernel.Set',
                            setting=setting,
                            value=value,
                            )
    def list(self, option=None):
        '''
        List VMkernel kernel settings.
        :param option: string, The name of the VMkernel kernel setting to get.
        :returns: vim.EsxCLI.system.settings.kernel.list.SettingsKernel[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.settings.kernel.List',
                            option=option,
                            )   