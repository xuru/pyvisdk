
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostHostBusAdapter(DynamicData):
    '''This data object type describes the bus adapter for the host. A host bus adapter
        (HBA) is a hardware or software adapter that connects the host to storage
        devices.
    '''
    
    def __init__(self, bus, device, driver, key, model, pci, status):
        # MUST define these
        super(HostHostBusAdapter, self).__init__()
    
        self.data['bus'] = bus
        self.data['device'] = device
        self.data['driver'] = driver
        self.data['key'] = key
        self.data['model'] = model
        self.data['pci'] = pci
        self.data['status'] = status
    
    
    @property
    def bus(self):
        '''The host bus number.
        '''
        return self.data['bus']

    @property
    def device(self):
        '''The device name of host bus adapter.
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
    def model(self):
        '''The model name of the host bus adapter.
        '''
        return self.data['model']

    @property
    def pci(self):
        '''The Peripheral Connect Interface (PCI) ID of the device representing the host bus
        adapter.
        '''
        return self.data['pci']

    @property
    def status(self):
        '''The operational status of the adapter. Valid values include "online", "offline",
        and "fault".
        '''
        return self.data['status']

