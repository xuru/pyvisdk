
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiIbftboot(Base):
    '''
    Operations that can be performed on iSCSI IBFT boot table
    '''
    moid = 'ha-cli-handler-iscsi-ibftboot'
    def import(self):
        '''
        Import iSCSI target configuration from iBFT to ESX iSCSI initiators. The boot target recorded in iBFT is added to all the eligible 'dependent' iSCSI adapters.
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.ibftboot.Import',
                            )
    def get(self):
        '''
        Get iSCSI IBFT Boot details.
        :returns: vim.EsxCLI.iscsi.ibftboot.get.IbftBoot[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.ibftboot.Get',
                            )   