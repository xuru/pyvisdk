
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkVswitchStandardPortgroupPolicyShaping(Base):
    '''
    Commands to manipulate shaping policy setting for the given portgroup.
    '''
    moid = 'ha-cli-handler-network-vswitch-standard-portgroup-policy-shaping'
    def set(self, portgroupname, avgbandwidth=None, burstsize=None, enabled=None, peakbandwidth=None, usevswitch=None):
        '''
        Set the shaping policy settings for the given port group
        :param avgbandwidth: long, The averge bandwidth allowed for this shaping policy. This value is in Kbps (1 Kbps = 1000 bits/s)
        :param burstsize: long, The largest burst size allowed for this shaping policy. This value is in Kib (1 Kib = 1024 bits)
        :param enabled: boolean, Indicate whether to enable traffic shaping on this policy. If this is true then the --avg-bandwidth, --peak-bandwidth and --burst-size options are required.
        :param peakbandwidth: long, The peak bandwidth allowed for this shaping policy. This value is in Kbps (1 Kbps = 1000 bits/s)
        :param portgroupname: string, The name of the port group to set shaping policy for.
        :param usevswitch: boolean, Reset all values for this policy to use parent virtual switch's settings instead of overriding the settings for the port group. Using this in conjunction with other settings will first reset all of the fields to use the virtual switch setting and then apply the other options after the reset.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.standard.portgroup.policy.shaping.Set',
                            avgbandwidth=avgbandwidth,
                            burstsize=burstsize,
                            enabled=enabled,
                            peakbandwidth=peakbandwidth,
                            portgroupname=portgroupname,
                            usevswitch=usevswitch,
                            )
    def get(self, portgroupname):
        '''
        Get the network shaping policy settings governing the given port group
        :param portgroupname: string, The name of the port group to use when fetching the port group shaping policy.
        :returns: vim.EsxCLI.network.vswitch.standard.portgroup.policy.shaping.get.PortGroupTrafficShapingPolicy
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.standard.portgroup.policy.shaping.Get',
                            portgroupname=portgroupname,
                            )   