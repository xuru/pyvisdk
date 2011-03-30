'''
Created on Feb 11, 2011

@author: eplaster
'''
import os.path
import sys

here = os.path.expanduser(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(here, ".."))

from pyvisdk import Vim
from pyvisdk.managedObjects.vm import VirtualMachine


filename = os.path.abspath(os.path.expanduser("~/.visdkrc.ksvcenter"))

credentials = {}
ident = open(filename).readlines()
for line in ident:
    name, value = [x.strip() for x in line.split("=")]
    credentials[name] = value

vim = None

class TestVirtualMachines(object):
    @classmethod
    def setup_class(klass):
        global vim
        print "setup_class: %s" % klass
        vim = Vim(credentials["VI_SERVER"])
        vim.login(credentials["VI_USERNAME"], credentials["VI_PASSWORD"])
        
        
    @classmethod
    def teardown_class(klass):
        global vim
        print "teardown_class: %s" % klass
        vim.logout()
        
    def testGetAll(self):
        global vim
        vms = vim.getVirtualMachines()
        assert(vms and len(vms)>0)
        for vm in vms:
            assert(isinstance(vm, VirtualMachine))
        
    def testGetVirtualMachine(self):
        global vim
        
        name = 'test'
        vm = vim.getVirtualMachine(name)
        assert(vm != None)
        assert(isinstance(vm, VirtualMachine))
        

if __name__ == "__main__":
    import nose
    argv = ["", '--verbosity=3', '--detailed-errors', '--nologcapture']
    nose.runmodule(argv=argv)

    
