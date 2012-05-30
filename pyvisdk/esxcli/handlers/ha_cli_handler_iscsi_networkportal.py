
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiNetworkportal(Base):
    '''
    Operations that can be performed on iSCSI Network Portal (iSCSI vmknic)
    '''
    moid = 'ha-cli-handler-iscsi-networkportal'
    def add(self, adapter, nic, force=None):
        '''
        Add a network portal for iSCSI adapter
        :param adapter: string, The iSCSI adapter name.
        :param force: boolean, The force flag (force add of iSCSI vmknic even it's not compatible for iscsi multipathing)
        :param nic: string, The iSCSI network portal (bound vmknic)
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.networkportal.Add',
                            adapter=adapter,
                            force=force,
                            nic=nic,
                            )
    def list(self, adapter=None):
        '''
        List Network Portal for iSCSI Adapter
        :param adapter: string, The iSCSI adapter name.
        :returns: vim.EsxCLI.iscsi.networkportal.list.NetworkPortal[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.networkportal.List',
                            adapter=adapter,
                            )
    def remove(self, adapter, nic, force=None):
        '''
        Remove a network portal for iSCSI adapter
        :param adapter: string, The iSCSI adapter name.
        :param force: boolean, The force flag (force removal of iSCSI vmknic when sessions are active using it)
        :param nic: string, The iSCSI network portal (bound vmknic)
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.networkportal.Remove',
                            adapter=adapter,
                            force=force,
                            nic=nic,
                            )   