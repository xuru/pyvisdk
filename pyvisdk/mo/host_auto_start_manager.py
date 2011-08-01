
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostAutoStartManager(BaseEntity):
    '''The AutoStartManager allows clients to invoke and set up the auto-start/auto-stop
        order of virtual machines on a single host. Virtual machines configured to
        use auto-start are automatically started or stopped when the host is
        started or shut down. The AutoStartManager is available when clients
        connect directly to a host, such as an ESX Server machine or through
        VirtualCenter.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostAutoStartManager):
        # MUST define these
        super(HostAutoStartManager, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def AutoStartPowerOff(self):
        '''Powers-off virtual machines according to the current AutoStart configuration.See
        the description of the (@link vim.host.AutoStartManager.AutoPowerInfo)
        data object type for more information on Auto power-off behavior.
        '''
        
        return self.delegate("AutoStartPowerOff")()
        

    def ReconfigureAutostart(self, spec):
        '''Changes the power-on or power-off sequence and system defaults. The specification
        is an incremental change to the current configuration.If systemDefaults
        are included, only values that are specified in the specification are
        changed.For the spec.powerInfo array, each element is interpreted as an
        incremental change and the changes are processed sequentially. It is not
        an error to remove a non-existing virtual machine. If both startAction and
        stopAction are set to none, then the virtual machine is removed from the
        configuration.A virtual machine's position in the order can be changed
        either by assigning the virtual machine a different position in the order
        or removing the machine from the order. When a virtual machine's position
        changes, all other virtual machines' positions may be affected as they
        move to new positions relative to each other.

        :param spec: List of changes to defaults and auto-start/auto-stop order.

        '''
        
        return self.delegate("ReconfigureAutostart")(spec)
        

    def AutoStartPowerOn(self):
        '''Powers-on virtual machines according to the current AutoStart configuration.See
        the description of the (@link vim.host.AutoStartManager.AutoPowerInfo)
        data object type for more information on Auto power-on behavior.
        '''
        
        return self.delegate("AutoStartPowerOn")()
        
