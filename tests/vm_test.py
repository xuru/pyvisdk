'''
Created on Feb 11, 2011

@author: eplaster
'''
import unittest
from pyvisdk import Vim
from pyvisdk.mo.virtual_machine import VirtualMachine
from pyvisdk.mo.folder import Folder
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

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSnapshot']
    unittest.main()
    
