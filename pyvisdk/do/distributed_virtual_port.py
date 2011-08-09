
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualPort(DynamicData):
    '''The data object that represents a port in the distributed virtual switch.
    '''
    
    def __init__(self, config, conflict, conflictPortKey, connectee, connectionCookie, dvsUuid, key, lastStatusChange, portgroupKey, proxyHost, state):
        # MUST define these
        super(DistributedVirtualPort, self).__init__()
    
        self.data['config'] = config
        self.data['conflict'] = conflict
        self.data['conflictPortKey'] = conflictPortKey
        self.data['connectee'] = connectee
        self.data['connectionCookie'] = connectionCookie
        self.data['dvsUuid'] = dvsUuid
        self.data['key'] = key
        self.data['lastStatusChange'] = lastStatusChange
        self.data['portgroupKey'] = portgroupKey
        self.data['proxyHost'] = proxyHost
        self.data['state'] = state
    
    
    @property
    def config(self):
        '''The management configuration of the port.
        '''
        return self.data['config']

    @property
    def conflict(self):
        '''Whether the port is a conflict port. A port could be marked as conflict if an
        entity is discovered connecting to a port that is already occupied, or if
        the port is created by the host without conferring with vCenter Server. A
        conflict port will not have its runtime state persisted and the port can't
        move away from the host, that is, no VMotion if a Virtual Machine is using
        a conflict port.
        '''
        return self.data['conflict']

    @property
    def conflictPortKey(self):
        '''If the port is marked conflict in the case of two entities connecting to the same
        port (see conflict), this is the key of the port which the connected
        entity is contending for.
        '''
        return self.data['conflictPortKey']

    @property
    def connectee(self):
        '''The entity that connects to the port.
        '''
        return self.data['connectee']

    @property
    def connectionCookie(self):
        '''This is a cookie representing the current instance of association between port and
        vNIC/pNIC (which is represented as DistributedVirtualSwitchPortConnection
        objects). The same cookie is present on the pNIC/vNIC configuration (see
        connectionCookie) in order for the port to authenticate that the peer is
        the rightful connectee of the port.
        '''
        return self.data['connectionCookie']

    @property
    def dvsUuid(self):
        '''The UUID of DistributedVirtualSwitch that the port belongs to.
        '''
        return self.data['dvsUuid']

    @property
    def key(self):
        '''The port key.
        '''
        return self.data['key']

    @property
    def lastStatusChange(self):
        '''The last time the runtimeInfo value was changed.
        '''
        return self.data['lastStatusChange']

    @property
    def portgroupKey(self):
        '''The key of the portgroup that the port belongs to, if any.
        '''
        return self.data['portgroupKey']

    @property
    def proxyHost(self):
        '''The host that services this port
        '''
        return self.data['proxyHost']

    @property
    def state(self):
        '''The runtime state of the port.
        '''
        return self.data['state']

