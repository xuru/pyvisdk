
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkVswitchStandardPolicyShaping(Base):
    '''
    Commands to manipulate shaping policy setting for the given virtual switch.
    '''
    moid = 'ha-cli-handler-network-vswitch-standard-policy-shaping'
    def set(self, vswitchname, avgbandwidth=None, burstsize=None, enabled=None, peakbandwidth=None):
        '''
        Set the shaping policy settings for the given virtual switch
        :param avgbandwidth: long, The averge bandwidth allowed for this shaping policy. This value is in Kbps (1 Kbps = 1000 bits/s)
        :param burstsize: long, The largest burst size allowed for this shaping policy. This value is in Kib (1 Kib = 1024 bits)
        :param enabled: boolean, Indicate whether to enable traffic shaping on this policy. If this is true then the --avg-bandwidth, --peak-bandwidth and --burst-size options are required.
        :param peakbandwidth: long, The peak bandwidth allowed for this shaping policy. This value is in Kbps (1 Kbps = 1000 bits/s)
        :param vswitchname: string, The name of the virtual switch to use when setting the switch shaping policy.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.standard.policy.shaping.Set',
                            avgbandwidth=avgbandwidth,
                            burstsize=burstsize,
                            enabled=enabled,
                            peakbandwidth=peakbandwidth,
                            vswitchname=vswitchname,
                            )
    def get(self, vswitchname):
        '''
        Get the shaping policy settings for the given virtual switch
        :param vswitchname: string, The name of the virtual switch to use when fetching the switch shaping policy.
        :returns: vim.EsxCLI.network.vswitch.standard.policy.shaping.get.VirtualSwitchTrafficShapingPolicy
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.vswitch.standard.policy.shaping.Get',
                            vswitchname=vswitchname,
                            )   