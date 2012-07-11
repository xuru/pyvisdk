'''
Created on Jul 6, 2011

@author: eplaster
'''
import unittest
from pyvisdk import Vim
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from tests.common import get_options

class TestDatacenter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.options = get_options()
        cls.vim = Vim(cls.options.server)
        cls.vim.login(cls.options.username, cls.options.password)

    @classmethod
    def tearDownClass(cls):
        cls.vim.logout()

    def testDatacenters(self):
        dcs = self.vim.getDatacenters()
        self.assertGreaterEqual(len(dcs), 1, "vcenter has no datacenters")
        
    def testDatacenter(self):
        dcs = self.vim.getDatacenters()
        self.assertGreaterEqual(len(dcs), 1, "vcenter has no datacenters")
        
        _name = dcs[0].name
        dc = self.vim.getDatacenter(_name)
        self.assertIsNotNone(dc, "Couldn't get DC: %s" % _name)
        self.assertEqual(dc._type, ManagedObjectTypes.Datacenter, "Datacenter's type isn't Datacenter...")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDatacenter']
    unittest.main()
