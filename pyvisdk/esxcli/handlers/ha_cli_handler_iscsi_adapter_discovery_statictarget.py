
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiAdapterDiscoveryStatictarget(Base):
    '''
    Operations that can be performed on iSCSI statictarget discovery
    '''
    moid = 'ha-cli-handler-iscsi-adapter-discovery-statictarget'
    def add(self, adapter, address, name):
        '''
        Add a static target address
        :param adapter: string, The iSCSI adapter name.
        :param address: string, The iSCSI target address: <ip/dns[:port]>
        :param name: string, The iSCSI target name.
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.discovery.statictarget.Add',
                            adapter=adapter,
                            address=address,
                            name=name,
                            )
    def list(self, adapter=None):
        '''
        List static target addresses
        :param adapter: string, The iSCSI adapter name.
        :returns: vim.EsxCLI.iscsi.adapter.discovery.statictarget.list.Statictarget[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.discovery.statictarget.List',
                            adapter=adapter,
                            )
    def remove(self, adapter, address, name):
        '''
        Remove a static target
        :param adapter: string, The iSCSI adapter name.
        :param address: string, The iSCSI target address: <ip/dns[:port]>
        :param name: string, The iSCSI target name.
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.discovery.statictarget.Remove',
                            adapter=adapter,
                            address=address,
                            name=name,
                            )   