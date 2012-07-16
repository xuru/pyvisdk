
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiAdapterDiscoverySendtarget(Base):
    '''
    Operations that can be performed on iSCSI sendtargets discovery
    '''
    moid = 'ha-cli-handler-iscsi-adapter-discovery-sendtarget'
    def add(self, adapter, address):
        '''
        Add a sendtarget address
        :param adapter: string, The iSCSI adapter name.
        :param address: string, The iSCSI sendtarget address: <ip/dns[:port]>
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.discovery.sendtarget.Add',
                            adapter=adapter,
                            address=address,
                            )
    def list(self, adapter=None):
        '''
        List sendtarget addresses
        :param adapter: string, The iSCSI adapter name.
        :returns: vim.EsxCLI.iscsi.adapter.discovery.sendtarget.list.Sendtarget[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.discovery.sendtarget.List',
                            adapter=adapter,
                            )
    def remove(self, adapter, address):
        '''
        Remove a sendtarget address
        :param adapter: string, The iSCSI adapter name.
        :param address: string, The iSCSI sendtarget address: <ip/dns[:port]>
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.discovery.sendtarget.Remove',
                            adapter=adapter,
                            address=address,
                            )   