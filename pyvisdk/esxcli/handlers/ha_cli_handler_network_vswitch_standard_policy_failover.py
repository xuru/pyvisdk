
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkVswitchStandardPolicyFailover(Base):
    '''
    Commands to manipulate failover policy setting for the given virtual switch.
    '''
    moid = 'ha-cli-handler-network-vswitch-standard-policy-failover'
    def set(self, vswitchname, activeuplinks=None, failback=None, failuredetection=None, loadbalancing=None, notifyswitches=None, standbyuplinks=None):
        '''
        Configure the Failover policy for a virtual switch.
        :param activeuplinks: string, Configure the list of active adapters and their failover order. This list must be a comma seperated list of values with the uplink name and no spaces. Example:  --active-uplinks=vmnic0,vmnic3,vmnic7,vmnic1
        :param failback: boolean, Configure whether a NIC will be used immediately when it comes back in service after a failover
        :param failuredetection: string, Set the method of determining how a network outage is detected. 
    beacon: Detect failures based on active beaconing to the vswitch
    link: Detect failures based on the NIC link state

        :param loadbalancing: string, Set the load balancing policy for this policy. This can be one of the following options: 
    explicit: Always use the highest order uplink from the list of active adapters which pass failover criteria.
    iphash: Route based on hashing the src and destination IP addresses
    mac: Route based on the MAC address of the packet source.
    portid: Route based on the originating virtual port ID.

        :param notifyswitches: boolean, Indicate whether to send a notification to physical switches on failover
        :param standbyuplinks: string, Configure the list of standby adapters and their failover order. This list must be a comma seperated list of values with the uplink name and no spaces. Example:  --standby-uplinks=vmnic2,vmnic4,vmnic8,vmnic6,vmnic11
        :param vswitchname: string, The name of the virtual switch to use when configuring the switch failover policy.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.standard.policy.failover.Set',
                            activeuplinks=activeuplinks,
                            failback=failback,
                            failuredetection=failuredetection,
                            loadbalancing=loadbalancing,
                            notifyswitches=notifyswitches,
                            standbyuplinks=standbyuplinks,
                            vswitchname=vswitchname,
                            )
    def get(self, vswitchname):
        '''
        Get the failover policy settings governing the given virtual switch
        :param vswitchname: string, The name of the virtual switch to use when fetching the switch failover policy.
        :returns: vim.EsxCLI.network.vswitch.standard.policy.failover.get.VirtualSwitchFailoverPolicy
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.standard.policy.failover.Get',
                            vswitchname=vswitchname,
                            )   