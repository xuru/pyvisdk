# cython: profile=True

import logging
from vixDiskLib import *

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

class VDDKError(Exception):
    pass

class VixDiskLib(VixDiskLibBase):
    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.diskPath = ""
        self.info = ""
        self.connected = False
    
    def connect(self, vmname, snapshotRef, readonly = False):
        log.debug("Connecting to %s as %s" % (self.hostname, self.username))
        
        # call the C code to connect
        self._connect(vmname, self.hostname, self.username, self.password, snapshotRef, readonly)
        self.connected = True
        
    def getInfo(self):
        return self._getInfo()

    def copyFromVMDK(self, source_drive, destination, startSector, flags=VIXDISKLIB_FLAG_OPEN_READ_ONLY, append=False, numSectors=None):
        self.diskPath = source_drive
        
        # open the source vmdk
        self._open(source_drive, flags)
        fp = open(destination, 'wb')
        if not fp:
            raise IOError("Unable to open %s for writing." % destination)
        
        if not numSectors:
            if not self.info:
                self.getInfo() 
            numSectors = self.info["physGeo"]["sectors"]
            
        for index in range(numSectors):
            try:
                data = self._read(startSector+index)
            except VixDiskLibError, e:
                self._close()
                raise
            fp.write(data)
        self._close()
        
    def close(self):
        self._close()

    def disconnect(self):
        log.debug("Disconnecting from %s" % self.hostname)
        self._disconnect()
        self.connected = False
    
# ----------------------------------------------------------------------
# vim: set filetype=python expandtab shiftwidth=4:
# [X]Emacs local variables declaration - place us into python mode
# Local Variables:
# mode:python
# py-indent-offset:4
# End: