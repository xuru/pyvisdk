
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiAdapterCapabilities(Base):
    '''
    Operations that can be performed on iSCSI adapter capabilities
    '''
    moid = 'ha-cli-handler-iscsi-adapter-capabilities'
    def get(self, adapter):
        '''
        List the iSCSI details for the iSCSI Host Bus Adapter.
        :param adapter: string, The iSCSI adapter name.
        :returns: vim.EsxCLI.iscsi.adapter.capabilities.get.AdapterCapabilities[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.capabilities.Get',
                            adapter=adapter,
                            )   