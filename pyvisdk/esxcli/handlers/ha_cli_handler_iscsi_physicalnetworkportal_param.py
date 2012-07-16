
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiPhysicalnetworkportalParam(Base):
    '''
    Operations that can be performed on iSCSI Physical Network Portal (vmnic)'s parameters
    '''
    moid = 'ha-cli-handler-iscsi-physicalnetworkportal-param'
    def set(self, adapter, enabled, option, nic=None):
        '''
        Set network parameter on a Physical Network Portal
        :param adapter: string, The iSCSI adapter name.
        :param enabled: boolean, Enable or disable a Physical Network Portal option
        :param nic: string, The physical network portal name: <vmnic>
        :param option: string, The network parameter option
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.physicalnetworkportal.param.Set',
                            adapter=adapter,
                            enabled=enabled,
                            nic=nic,
                            option=option,
                            )
    def get(self, adapter, nic=None):
        '''
        Get network parameters on a Physical Network Portal (vmnic)
        :param adapter: string, The iSCSI adapter name.
        :param nic: string, The physical network portal name: <vmnic>
        :returns: vim.EsxCLI.iscsi.physicalnetworkportal.param.get.iScsiNetParm[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.physicalnetworkportal.param.Get',
                            adapter=adapter,
                            nic=nic,
                            )   