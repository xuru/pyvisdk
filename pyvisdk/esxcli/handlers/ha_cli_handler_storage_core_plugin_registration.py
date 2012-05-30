
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageCorePluginRegistration(Base):
    '''
    Operations pertaining to the pluggable storage architectures' plugin registration. The operations currently allowed are to list registered plugins on the system with the type of those plugins and to register and unregister plugin modules on the system
    '''
    moid = 'ha-cli-handler-storage-core-plugin-registration'
    def add(self, modulename, pluginclass, pluginname, dependencies=None, fullpath=None):
        '''
        Register a plugin module with PSA.
        :param dependencies: string, Add the [optional] dependencies for this module to loaded
        :param fullpath: string, Add the [optional] full path to this module
        :param modulename: string, Select the module name to be registered
        :param pluginclass: string, Indicate the class of plugin to register.  Allowed values are MP, VAAI or MPP defined subplugins like PSP, SATP.
        :param pluginname: string, Select the plugin name to be registered
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.plugin.registration.Add',
                            dependencies=dependencies,
                            fullpath=fullpath,
                            modulename=modulename,
                            pluginclass=pluginclass,
                            pluginname=pluginname,
                            )
    def list(self, modulename=None, pluginclass=None):
        '''
        List modules currently registered with PSA.
        :param modulename: string, Filter the output of this command to only show a single module.
        :param pluginclass: string, Indicate the class of plugin to list.  Allowed values are MP, VAAI or MPP defined subplugins like PSP, SATP.
        :returns: vim.EsxCLI.storage.core.plugin.registration.list.RegisteredModuleList[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.plugin.registration.List',
                            modulename=modulename,
                            pluginclass=pluginclass,
                            )
    def remove(self, modulename):
        '''
        UnRegister a plugin module with PSA.
        :param modulename: string, Select the module name to be unregistered
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.plugin.registration.Remove',
                            modulename=modulename,
                            )   