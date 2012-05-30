
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiNetworkportalIpconfig(Base):
    '''
    Operations that can be performed on iSCSI Network Portal (iSCSI vmknic)'s IP configuration
    '''
    moid = 'ha-cli-handler-iscsi-networkportal-ipconfig'
    def set(self, adapter, ip, subnet, dns1=None, dns2=None, gateway=None, nic=None):
        '''
        Set iSCSI network portal IP configuration
        :param adapter: string, The iSCSI adapter name.
        :param dns1: string, The iSCSI network portal primary DNS address
        :param dns2: string, The iSCSI network portal secondary DNS address
        :param gateway: string, The iSCSI network portal gateway address
        :param ip: string, The iSCSI network portal IP address
        :param nic: string, The iSCSI network portal (vmknic)
        :param subnet: string, The iSCSI network portal subnet mask
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.networkportal.ipconfig.Set',
                            adapter=adapter,
                            dns1=dns1,
                            dns2=dns2,
                            gateway=gateway,
                            ip=ip,
                            nic=nic,
                            subnet=subnet,
                            )
    def get(self, adapter, nic=None):
        '''
        Get iSCSI network portal ip configuration
        :param adapter: string, The iSCSI adapter name.
        :param nic: string, The iSCSI network portal (vmknic)
        :returns: vim.EsxCLI.iscsi.networkportal.ipconfig.get.NetworkPortal[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.networkportal.ipconfig.Get',
                            adapter=adapter,
                            nic=nic,
                            )   