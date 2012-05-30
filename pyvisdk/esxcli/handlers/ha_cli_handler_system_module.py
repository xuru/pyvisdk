
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemModule(Base):
    '''
    Operations that allow manipulation of the VMkernel loadable modules and device drivers. Operations include load, list and setting options.
    '''
    moid = 'ha-cli-handler-system-module'
    def load(self, module, force=None):
        '''
        Load a VMkernel module with the given name if it is enabled. If the module is disabled then the use of --force is required to load the module.
        :param force: boolean, Ignore the enabled/disabled state of this module and force it to load.
        :param module: string, The name of the VMkernel module to load.
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.module.Load',
                            force=force,
                            module=module,
                            )
    def set(self, enabled, module, force=None):
        '''
        Allow enabling and disabling of a VMkernel module.
        :param enabled: boolean, Set to true to enable the module, set to false to disable the module.
        :param force: boolean, Skip VMkernel module validity checks and set options for a module (or alias) with the given name.
        :param module: string, The name of the VMkernel module to set options for.
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.module.Set',
                            enabled=enabled,
                            force=force,
                            module=module,
                            )
    def list(self, enabled=None, loaded=None):
        '''
        List the VMkernel modules that the system knows about.
        :param enabled: boolean, List the enabled / disabled VMkernel modules and device drivers.
        :param loaded: boolean, List the loaded / not loaded VMkernel modules and device drivers.
        :returns: vim.EsxCLI.system.module.list.Module[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.module.List',
                            enabled=enabled,
                            loaded=loaded,
                            )
    def get(self, module):
        '''
        Show the ELF header information for the given VMkernel module.
        :param module: string, The name of the VMkernel module to get the option string for.
        :returns: vim.EsxCLI.system.module.get.ModuleDetails
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.module.Get',
                            module=module,
                            )   