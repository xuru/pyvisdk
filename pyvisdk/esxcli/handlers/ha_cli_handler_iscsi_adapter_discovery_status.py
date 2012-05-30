
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiAdapterDiscoveryStatus(Base):
    '''
    Operations that can be performed on iSCSI adapter discovery status
    '''
    moid = 'ha-cli-handler-iscsi-adapter-discovery-status'
    def get(self, adapter):
        '''
        Get the iSCSI adapter discovery status for the iSCSI Host Bus Adapter.
        :param adapter: string, The iSCSI adapter name.
        :returns: string
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.discovery.status.Get',
                            adapter=adapter,
                            )   