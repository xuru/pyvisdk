'''
Created on Mar 8, 2011

@author: eplaster
'''

from mangagedObjects.managedentity import ManagedEntity
from pyvisdk import consts
from pyvisdk.consts import ManagedObjectReference
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

class VirtualMachineSnapshot(ManagedEntity):
    def __init__(self, vm, name=None, ref=None):
        """ 
        VirtualMachineSnapshot
        
        Note: this is a special case in that we are not getting an MOR, but a VirtualMachineSnapshotTree
        in ref.  This is the only way to preserve the information gleened from the VirtualMachine "snapshot"
        properties.
        """
        self.data = ref
        self.vm = vm
        if ref:
            ref = ref.snapshot
        
        # MUST define these
        props = [ "configInfo" ]
        super(VirtualMachineSnapshot, self).__init__(vm.core, props, name, ref)
        
        self.type = consts.VirtualMachineSnapshot # type used to get to the virtual disks
        
        self.config = None
        self.name = name
        self.ref = ref
        if ref:
            self.ref = ManagedObjectReference(consts.VirtualMachineSnapshot, ref.value)
        self.parse()
        
    def update(self, prop):
        super(VirtualMachineSnapshot, self).update(prop)
        
        log.debug("*********** %s update **************" % self.__class__.__name__)
        for name, value in prop.items():
            if name == 'config':
                log.debug("[%s] %s" % (name, value.__class__.__name__))
                # VmfsDatastoreInfo
                self.config = value
            
    def parse(self):
        info = {}
        #info = self.core.getDynamicProperty(self.ref, self.props)
        self.update(info)
        
        if self.data:
            self.name = self.data.name
            self.description = self.data.description
            self.createTime = self.data.createTime
            self.state = self.data.state
            self.quiesced = self.data.quiesced
        
    def __str__(self):
        return "<%s> %s" % (self.type, self.name)
if __name__ == '__main__':
    import sys.path
    from os.path import join, abspath, dirname
    from pyvisdk.vim import Vim
    
    cpath = abspath(join(dirname(__file__), ".."))
    sys.path.insert(0, join(cpath, "pyvisdk"))
    
    vim = Vim("ksvcenter.kingcompanies.com")
    vim.login("admin-eplaster", "dew4u&me")
    
    for vm in vim.getAllVirtualMachinesIter():
        if not vm.hasSnapshots():
            print "Creating snapshot..."
            vm.createSnapshot()
        snapshot = vm.getSnapshots()[0]

    snapshot.queryChangedDiskAreas()
