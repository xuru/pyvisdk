
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiAdapterDiscovery(Base):
    '''
    Operations that can be performed on iSCSI adapter discovery
    '''
    moid = 'ha-cli-handler-iscsi-adapter-discovery'
    def rediscover(self, adapter):
        '''
        Do the iSCSI Discovery for the iSCSI Host Bus Adapter.
        :param adapter: string, The iSCSI adapter name.
        :returns: string
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.discovery.Rediscover',
                            adapter=adapter,
                            )   