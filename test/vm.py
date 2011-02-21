'''
Created on Feb 11, 2011

@author: eplaster
'''
import sys
import os.path

here = os.path.expanduser(os.path.dirname(__file__))
sys.path.insert(0, os.path.join("..", "src"))

from pyvisdk import Vim
from pyvisdk.vm import VirtualMachine

ident = open("ident.cnf").readlines()
server = ident[0].strip()
username = ident[1].strip()
password = ident[2].strip()

vim = None

class TestVirtualMachines(object):
    @classmethod
    def setup_class(klass):
        global vim
        print "setup_class: %s" % klass
        vim = Vim(server)
        vim.login(username, password)
        
        
    @classmethod
    def teardown_class(klass):
        global vim
        print "teardown_class: %s" % klass
        vim.logout()
        
    def testGetAll(self):
        global vim
        vms = vim.getAllVirtualMachines()
        assert(vms and len(vms)>0)
        for vm in vms:
            assert(isinstance(vm, VirtualMachine))
        
    def testGetVirtualMachine(self):
        global vim
        name = 'test'
        vm = vim.getVirtualMachine(name)
        assert(vm != None)
        assert(isinstance(vm, VirtualMachine))
        
    def testClone(self):
        pass

    def testCreate(self):
        pass

    def testGetSnapshots(self):
        name = 'test'
        vm = vim.getVirtualMachine(name)
        snapshots = vm.getSnapshots()
        
    def testCreateSnapshot(self):
        name = 'test'
        vm = vim.getVirtualMachine(name)
        vm.createSnapshot(vm.name + "000001")

    def testRemoveSnapshot(self):
        pass

    def testReconfigure(self):
        pass


if __name__ == "__main__":
    import nose
    argv = ["", '--verbosity=3', '--detailed-errors', '--nologcapture']
    nose.runmodule(argv=argv)

    
