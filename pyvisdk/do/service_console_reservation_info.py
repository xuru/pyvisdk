
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ServiceConsoleReservationInfo(DynamicData):
    '''The ServiceConsoleReservationInfo data object type describes the amount of memory
        that is being reserved by the service console. Memory reserved for use by
        the service console is a hard reservation that cannot be changed except
        across hardware restarts.This memory that is reserved for the service
        console is used primarily to provide system management services. In
        addition, a small overhead is needed by each virtual machine on the
        service console.The only property of the data object that can be changed
        directly is the serviceConsoleReservedCfg property. This property
        indicates how much memory should be reserved for the service console on
        the next boot. In most cases, this amount is the same as the current
        reservation.
    '''
    
    def __init__(self, serviceConsoleReserved, serviceConsoleReservedCfg, unreserved):
        # MUST define these
        super(ServiceConsoleReservationInfo, self).__init__()
    
        self.data['serviceConsoleReserved'] = serviceConsoleReserved
        self.data['serviceConsoleReservedCfg'] = serviceConsoleReservedCfg
        self.data['unreserved'] = unreserved
    
    
    @property
    def serviceConsoleReserved(self):
        '''The amount of memory that is currently reserved for the service console.
        '''
        return self.data['serviceConsoleReserved']

    @property
    def serviceConsoleReservedCfg(self):
        '''The amount of memory that should be reserved for the service console on the next
        boot.
        '''
        return self.data['serviceConsoleReservedCfg']

    @property
    def unreserved(self):
        '''The amount of memory that is not reserved for use by the service console.
        '''
        return self.data['unreserved']

