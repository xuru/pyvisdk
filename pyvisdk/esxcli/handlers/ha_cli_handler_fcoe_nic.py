
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class FcoeNic(Base):
    '''
    Operations that can be performed on FCOE-capable CNA devices
    '''
    moid = 'ha-cli-handler-fcoe-nic'
    def disable(self, nicname):
        '''
        Disable rediscovery of FCOE storage on behalf of an FCOE-capable CNA upon next boot.
        :param nicname: string, The CNA adapter name (vmnicX)
        :returns: string
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.fcoe.nic.Disable',
                            nicname=nicname,
                            )
    def list(self):
        '''
        List FCOE-capable CNA devices.
        :returns: vim.EsxCLI.fcoe.nic.list.NicDevice[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.fcoe.nic.List',
                            )
    def discover(self, nicname):
        '''
        Initiate FCOE adapter discovery on behalf of an FCOE-capable CNA.
        :param nicname: string, The CNA adapter name (vmnicX)
        :returns: string
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.fcoe.nic.Discover',
                            nicname=nicname,
                            )   