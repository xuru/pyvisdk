
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemModuleParameters(Base):
    '''
    Operations that allow manipulation of parameters of VMkernel loadable modules and device drivers. Operations include list and set options.
    '''
    moid = 'ha-cli-handler-system-module-parameters'
    def set(self, module, parameterstring, force=None):
        '''
        Set the load time parameters for the given VMkernel module.
        :param force: boolean, Skip VMkernel module validity checks and set parameters for a module (or alias) with the given name.
        :param module: string, The name of the VMkernel module to set parameters for.
        :param parameterstring: string, The string containing the parameters for this module.
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.module.parameters.Set',
                            force=force,
                            module=module,
                            parameterstring=parameterstring,
                            )
    def list(self, module):
        '''
        List the parameters, a descriptions of each parameter supported for a given module name and the user defined value for each parameter.
        :param module: string, The name of the VMkernel module to get the option string for.
        :returns: vim.EsxCLI.system.module.parameters.list.ModuleParameter[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.module.parameters.List',
                            module=module,
                            )   