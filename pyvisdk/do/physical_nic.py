
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PhysicalNic(DynamicData):
    '''This data object type describes the physical network adapter as seen by the
        primary operating system.
    '''
    
    def __init__(self, autoNegotiateSupported, device, driver, key, linkSpeed, mac, pci, resourcePoolSchedulerAllowed, resourcePoolSchedulerDisallowedReason, spec, validLinkSpecification, vmDirectPathGen2Supported, vmDirectPathGen2SupportedMode, wakeOnLanSupported):
        # MUST define these
        super(PhysicalNic, self).__init__()
    
        self.data['autoNegotiateSupported'] = autoNegotiateSupported
        self.data['device'] = device
        self.data['driver'] = driver
        self.data['key'] = key
        self.data['linkSpeed'] = linkSpeed
        self.data['mac'] = mac
        self.data['pci'] = pci
        self.data['resourcePoolSchedulerAllowed'] = resourcePoolSchedulerAllowed
        self.data['resourcePoolSchedulerDisallowedReason'] = resourcePoolSchedulerDisallowedReason
        self.data['spec'] = spec
        self.data['validLinkSpecification'] = validLinkSpecification
        self.data['vmDirectPathGen2Supported'] = vmDirectPathGen2Supported
        self.data['vmDirectPathGen2SupportedMode'] = vmDirectPathGen2SupportedMode
        self.data['wakeOnLanSupported'] = wakeOnLanSupported
    
    
    @property
    def autoNegotiateSupported(self):
        '''If set the flag indicates if the physical network adapter supports autonegotiate.
        '''
        return self.data['autoNegotiateSupported']

    @property
    def device(self):
        '''The device name of the physical network adapter.
        '''
        return self.data['device']

    @property
    def driver(self):
        '''The name of the driver.
        '''
        return self.data['driver']

    @property
    def key(self):
        '''The linkable identifier.
        '''
        return self.data['key']

    @property
    def linkSpeed(self):
        '''The current link state of the physical network adapter. If this object is not set,
        then the link is down.
        '''
        return self.data['linkSpeed']

    @property
    def mac(self):
        '''The media access control (MAC) address of the physical network adapter.
        '''
        return self.data['mac']

    @property
    def pci(self):
        '''Device hash of the PCI device corresponding to this physical network adapter.
        '''
        return self.data['pci']

    @property
    def resourcePoolSchedulerAllowed(self):
        '''Flag indicating whether the NIC allows resource pool based scheduling for network
        I/O control.
        '''
        return self.data['resourcePoolSchedulerAllowed']

    @property
    def resourcePoolSchedulerDisallowedReason(self):
        '''If resourcePoolSchedulerAllowed is false, this property advertises the reason for
        disallowing resource scheduling on this NIC. The reasons may be one of
        PhysicalNicResourcePoolSchedulerDisallowedReason
        '''
        return self.data['resourcePoolSchedulerDisallowedReason']

    @property
    def spec(self):
        '''The specification of the physical network adapter.
        '''
        return self.data['spec']

    @property
    def validLinkSpecification(self):
        '''The valid combinations of speed and duplexity for this physical network adapter.
        The speed and the duplex settings usually must be configured as a pair.
        This array lists all the valid combinations available for a physical
        network adapter.
        '''
        return self.data['validLinkSpecification']

    @property
    def vmDirectPathGen2Supported(self):
        '''Flag indicating whether the NIC supports VMDirectPath Gen 2. Note that this is
        only an indicator of the capabilities of this NIC, not of the whole host.
        '''
        return self.data['vmDirectPathGen2Supported']

    @property
    def vmDirectPathGen2SupportedMode(self):
        '''If vmDirectPathGen2Supported is true, this property advertises the VMDirectPath
        Gen 2 mode supported by this NIC (chosen from
        PhysicalNicVmDirectPathGen2SupportedMode). A mode may require that the
        associated vNetwork Distributed Switch have a particular ProductSpec in
        order for network passthrough to be possible.
        '''
        return self.data['vmDirectPathGen2SupportedMode']

    @property
    def wakeOnLanSupported(self):
        '''Flag indicating whether the NIC is wake-on-LAN capable
        '''
        return self.data['wakeOnLanSupported']

