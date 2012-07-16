
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkVswitchStandardUplink(Base):
    '''
    Commands to add and remove uplink on given virtual switch.
    '''
    moid = 'ha-cli-handler-network-vswitch-standard-uplink'
    def add(self, uplinkname, vswitchname):
        '''
        Add an uplink to the given virtual switch. Note if this virtual switch has a NIC teaming policy assigned to it then the policy must also be modified to enable use of this uplink on this virtual switch
        :param uplinkname: string, The name of the uplink to add to the virtual switch.
        :param vswitchname: string, The name of the virtual switch to add an uplink to.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.standard.uplink.Add',
                            uplinkname=uplinkname,
                            vswitchname=vswitchname,
                            )
    def remove(self, uplinkname, vswitchname):
        '''
        Remove an uplink from the given virtual switch. Note if this virtual switch has a NIC teaming policy assigned to it then the policy must also be modified to disable use of this uplink on this virtual switch
        :param uplinkname: string, The name of the uplink to remove from the virtual switch.
        :param vswitchname: string, The name of the virtual switch to remove an uplink from.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.standard.uplink.Remove',
                            uplinkname=uplinkname,
                            vswitchname=vswitchname,
                            )   