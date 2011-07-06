'''
Created on Feb 11, 2011

@author: eplaster
'''
import unittest
from pyvisdk import Vim
from pyvisdk.managedObjects.vm import VirtualMachine
from pyvisdk.managedObjects.folder import Folder
from tests.common import get_options


class TestVirtualMachines(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.options = get_options()
        cls.vim = Vim(cls.options.server)
        cls.vim.login(cls.options.username, cls.options.password)
        
    @classmethod
    def tearDownClass(cls):
        cls.vim.logout()
        
    def testVirtualMachines(self):
        vms = self.vim.getVirtualMachines()
        self.assertGreaterEqual(len(vms), 1, "vcenter has no virtual machines")
        
    def testVirtualMachine(self):
        vms = self.vim.getVirtualMachines()
        self.assertGreaterEqual(len(vms), 1, "vcenter has no virtual machines")
        
        _name = vms[0].name
        vm = self.vim.getVirtualMachine(_name)
        self.assertIsNotNone(vm, "Couldn't get VM: %s" % _name)
        self.assertEqual(vm.type, 'VirtualMachine', "Virtual machine's type isn't VirtualMachine...")
        
    def testMethods(self):
        vms = self.vim.getVirtualMachines()
        vm = self.vim.getVirtualMachine(vms[0].name)
        
        self.assertIsInstance(vm.methods, list, "VirtualMachine.methods is not a list")
        for method in vm.methods:
            self.assertTrue(hasattr(vm, method), "VirtualMachine doesn't have method %s" % method)
        
    def testProps(self):
        vms = self.vim.getVirtualMachines()
        for vm in vms:
            self.assertIsInstance(vm, VirtualMachine, "Not an VirtualMachine instance")
            self.assertIsNotNone(vm.props, "props is None")
            
            # test each possible prop for the right object type
            for prop in vm.props:
                # first three are common props
                if prop in ["configIssue", "configStatus"]:
                    self.assertIsNotNone(eval("vm.%s" % prop), "Prop %s is None." % prop)
                elif prop == "name":
                    self.assertGreaterEqual(len(vm.name), 1, "Name has no length...")
                elif prop == "parent":
                    self.assertIsInstance(vm.parent, Folder, "parent prop is not a Folder instance")
                    
                elif prop in ['capability', 'config', 'datastore', 'environmentBrowser', 'guest', 'guestHeartbeatStatus', \
                     'layout', 'layoutEx', 'network', 'resourcePool', \
                     'rootSnapshot', 'runtime', 'storage', 'summary']:
                    self.assertIsNotNone(eval("vm.%s" % prop), "%s is None" % prop)

                else:
                    print "Untested prop: %s" % prop

    def testHasSnapShots(self):
        vm = self.vim.getVirtualMachines()[0]
        self.assertIsNotNone(vm.hasSnapshots(), "vm.hassnapshots() returned None...")
        
    def testGetSnapshots(self):
        vm = self.vim.getVirtualMachines()[0]
        self.assertIsInstance(vm.getSnapshots(), list, "vm.getSnapshots() returned something other then a list")
        
        
        
if __name__ == "__main__":
    import nose
    argv = ["", '--verbosity=3', '--detailed-errors', '--nologcapture']
    nose.runmodule(argv=argv)

    
