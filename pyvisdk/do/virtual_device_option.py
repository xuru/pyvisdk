
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDeviceOption(DynamicData):
    '''The VirtualDeviceOption data object type contains information about a virtual
        device type, the options for configuring the virtual device, and the
        relationship between this virtual device and other devices. The vSphere
        API groups device configurations that are mutually exclusive into
        different configuration objects; each of these configuration objects may
        define subtypes for virtual device backing options that are independent of
        the virtual device. Backing-dependent options should appear in a subtype
        of VirtualDeviceBackingOption.
    '''
    
    def __init__(self, autoAssignController, backingOption, connectOption, controllerType, defaultBackingOptionIndex, deprecated, hotRemoveSupported, licensingLimit, plugAndPlay, type):
        # MUST define these
        super(VirtualDeviceOption, self).__init__()
    
        self.data['autoAssignController'] = autoAssignController
        self.data['backingOption'] = backingOption
        self.data['connectOption'] = connectOption
        self.data['controllerType'] = controllerType
        self.data['defaultBackingOptionIndex'] = defaultBackingOptionIndex
        self.data['deprecated'] = deprecated
        self.data['hotRemoveSupported'] = hotRemoveSupported
        self.data['licensingLimit'] = licensingLimit
        self.data['plugAndPlay'] = plugAndPlay
        self.data['type'] = type
    
    
    @property
    def autoAssignController(self):
        '''Flag to indicate whether or not this device will be auto-assigned a controller if
        one is required. If this is true, then a client need not explicitly create
        the controller that this device will plug into.
        '''
        return self.data['autoAssignController']

    @property
    def backingOption(self):
        '''A list of backing options that can be used to map the virtual device to the host.
        The list is optional, since some devices exist only within the virtual
        machine; for example, a VirtualController.
        '''
        return self.data['backingOption']

    @property
    def connectOption(self):
        '''If the device is connectable, then the connectOption describes the connect options
        and defaults.
        '''
        return self.data['connectOption']

    @property
    def controllerType(self):
        '''Data object type that denotes the controller option object that is valid for
        controlling this device.
        '''
        return self.data['controllerType']

    @property
    def defaultBackingOptionIndex(self):
        '''Index into the backingOption list, indicating the default backing.
        '''
        return self.data['defaultBackingOptionIndex']

    @property
    def deprecated(self):
        '''Indicates whether this device is deprecated. Hence, if set the device cannot be
        used when creating a new virtual machine or be added to an existing
        virtual machine. However, the device is still supported by the platform.
        '''
        return self.data['deprecated']

    @property
    def hotRemoveSupported(self):
        '''Indicates if this type of device can be hot-removed from the virtual machine via a
        reconfigure operation when the virtual machine is powered on.
        '''
        return self.data['hotRemoveSupported']

    @property
    def licensingLimit(self):
        '''List of property names enforced by a licensing restriction of the underlying
        product. For example, a limit that is not derived based on the product or
        hardware features; the property name "numCPU".
        '''
        return self.data['licensingLimit']

    @property
    def plugAndPlay(self):
        '''Indicates if this type of device can be hot-added to the virtual machine via a
        reconfigure operation when the virtual machine is powered on.
        '''
        return self.data['plugAndPlay']

    @property
    def type(self):
        '''The name of the run-time class the client should instantiate to create a run-time
        instance of this device.
        '''
        return self.data['type']

