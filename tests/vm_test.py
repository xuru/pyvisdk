'''
Created on Feb 11, 2011

@author: eplaster
'''
import unittest
from pyvisdk import Vim
from pyvisdk.base.managed_object_types import ManagedObjectTypes
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
        self.assertEqual(vm._type, ManagedObjectTypes.VirtualMachine, "Virtual machine's type isn't VirtualMachine...")
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSnapshot']
    unittest.main()
    
