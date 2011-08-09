
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitchPortStatistics(DynamicData):
    '''Statistic data of a DistributedVirtualPort.
    '''
    
    def __init__(self, bytesInBroadcast, bytesInMulticast, bytesInUnicast, bytesOutBroadcast, bytesOutMulticast, bytesOutUnicast, packetsInBroadcast, packetsInDropped, packetsInException, packetsInMulticast, packetsInUnicast, packetsOutBroadcast, packetsOutDropped, packetsOutException, packetsOutMulticast, packetsOutUnicast):
        # MUST define these
        super(DistributedVirtualSwitchPortStatistics, self).__init__()
    
        self.data['bytesInBroadcast'] = bytesInBroadcast
        self.data['bytesInMulticast'] = bytesInMulticast
        self.data['bytesInUnicast'] = bytesInUnicast
        self.data['bytesOutBroadcast'] = bytesOutBroadcast
        self.data['bytesOutMulticast'] = bytesOutMulticast
        self.data['bytesOutUnicast'] = bytesOutUnicast
        self.data['packetsInBroadcast'] = packetsInBroadcast
        self.data['packetsInDropped'] = packetsInDropped
        self.data['packetsInException'] = packetsInException
        self.data['packetsInMulticast'] = packetsInMulticast
        self.data['packetsInUnicast'] = packetsInUnicast
        self.data['packetsOutBroadcast'] = packetsOutBroadcast
        self.data['packetsOutDropped'] = packetsOutDropped
        self.data['packetsOutException'] = packetsOutException
        self.data['packetsOutMulticast'] = packetsOutMulticast
        self.data['packetsOutUnicast'] = packetsOutUnicast
    
    
    @property
    def bytesInBroadcast(self):
        '''The number of bytes received from broadcast packets.
        '''
        return self.data['bytesInBroadcast']

    @property
    def bytesInMulticast(self):
        '''The number of bytes received from multicast packets.
        '''
        return self.data['bytesInMulticast']

    @property
    def bytesInUnicast(self):
        '''The number of bytes received from unicast packets.
        '''
        return self.data['bytesInUnicast']

    @property
    def bytesOutBroadcast(self):
        '''The number of bytes forwarded from broadcast packets.
        '''
        return self.data['bytesOutBroadcast']

    @property
    def bytesOutMulticast(self):
        '''The number of bytes forwarded from multicast packets.
        '''
        return self.data['bytesOutMulticast']

    @property
    def bytesOutUnicast(self):
        '''The number of bytes forwarded from unicast packets.
        '''
        return self.data['bytesOutUnicast']

    @property
    def packetsInBroadcast(self):
        '''The number of broadcast packets received.
        '''
        return self.data['packetsInBroadcast']

    @property
    def packetsInDropped(self):
        '''The number of received packets dropped.
        '''
        return self.data['packetsInDropped']

    @property
    def packetsInException(self):
        '''The number of packets received that cause an exception.
        '''
        return self.data['packetsInException']

    @property
    def packetsInMulticast(self):
        '''The number of multicast packets received.
        '''
        return self.data['packetsInMulticast']

    @property
    def packetsInUnicast(self):
        '''The number of unicast packets received.
        '''
        return self.data['packetsInUnicast']

    @property
    def packetsOutBroadcast(self):
        '''The number of broadcast packets forwarded.
        '''
        return self.data['packetsOutBroadcast']

    @property
    def packetsOutDropped(self):
        '''The number of packets to be forwarded dropped.
        '''
        return self.data['packetsOutDropped']

    @property
    def packetsOutException(self):
        '''The number of packets to be forwarded that cause an exception.
        '''
        return self.data['packetsOutException']

    @property
    def packetsOutMulticast(self):
        '''The number of multicast packets forwarded.
        '''
        return self.data['packetsOutMulticast']

    @property
    def packetsOutUnicast(self):
        '''The number of unicast packets forwarded.
        '''
        return self.data['packetsOutUnicast']

