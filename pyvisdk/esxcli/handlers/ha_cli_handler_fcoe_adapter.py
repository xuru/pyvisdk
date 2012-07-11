
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class FcoeAdapter(Base):
    '''
    Operations that can be performed on FCOE-type storage HBAs
    '''
    moid = 'ha-cli-handler-fcoe-adapter'
    def list(self):
        '''
        List FCOE-capable CNA devices.
        :returns: vim.EsxCLI.fcoe.adapter.list.FcoeAdapterDevice[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.fcoe.adapter.List',
                            )   