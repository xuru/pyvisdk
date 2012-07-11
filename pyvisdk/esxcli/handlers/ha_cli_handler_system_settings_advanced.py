
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemSettingsAdvanced(Base):
    '''
    The advanced settings are a set of VMkernel options that specific configuration settings to be modified. These options are typically in place for specific workarounds or debugging.
    '''
    moid = 'ha-cli-handler-system-settings-advanced'
    def set(self, option, default=None, intvalue=None, stringvalue=None):
        '''
        Set the value of an advanced option.
        :param default: boolean, Reset the option to its default value.
        :param intvalue: long, If the option is an integer value use this option.
        :param option: string, The name of the option to set the value of. Example: "/Misc/HostName"
        :param stringvalue: string, If the option is a string use this option.
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.settings.advanced.Set',
                            default=default,
                            intvalue=intvalue,
                            option=option,
                            stringvalue=stringvalue,
                            )
    def list(self, option=None, tree=None):
        '''
        List the advanced options available from the VMkernel.
        :param option: string, Only get the information for a single VMkernel advanced option.
        :param tree: string, Limit the list of advanced option to a specific sub tree.
        :returns: vim.EsxCLI.system.settings.advanced.list.SettingsAdvancedOption[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.settings.advanced.List',
                            option=option,
                            tree=tree,
                            )   