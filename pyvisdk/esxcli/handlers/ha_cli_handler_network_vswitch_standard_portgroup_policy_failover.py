
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkVswitchStandardPortgroupPolicyFailover(Base):
    '''
    Commands to manipulate failover policy setting for the given portgroup.
    '''
    moid = 'ha-cli-handler-network-vswitch-standard-portgroup-policy-failover'
    def set(self, portgroupname, activeuplinks=None, failback=None, failuredetection=None, loadbalancing=None, notifyswitches=None, standbyuplinks=None, usevswitch=None):
        '''
        Configure the Failover policy for a port group. These setting may potentially override virtual switch settings.
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
        :param portgroupname: string, The name of the port group to set failover policy for.
        :param standbyuplinks: string, Configure the list of standby adapters and their failover order. This list must be a comma seperated list of values with the uplink name and no spaces. Example:  --standby-uplinks=vmnic2,vmnic4,vmnic8,vmnic6,vmnic11
        :param usevswitch: boolean, Reset all values for this policy to use parent virtual switch's settings instead of overriding the settings for the port group. Using this in conjunction with other settings will first reset all of the fields to use the virtual switch setting and then apply the other options after the reset.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.standard.portgroup.policy.failover.Set',
                            activeuplinks=activeuplinks,
                            failback=failback,
                            failuredetection=failuredetection,
                            loadbalancing=loadbalancing,
                            notifyswitches=notifyswitches,
                            portgroupname=portgroupname,
                            standbyuplinks=standbyuplinks,
                            usevswitch=usevswitch,
                            )
    def get(self, portgroupname):
        '''
        Get the network failover policy settings governing the given port group
        :param portgroupname: string, The name of the port group to use when fetching the port group failover policy.
        :returns: vim.EsxCLI.network.vswitch.standard.portgroup.policy.failover.get.PortGroupFailoverPolicy
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.standard.portgroup.policy.failover.Get',
                            portgroupname=portgroupname,
                            )   